"""
--- Day 18: Duet ---
You discover a tablet containing some strange assembly code labeled simply "Duet". Rather than bother the sound card with it, you decide to run the code yourself. Unfortunately, you don't see any documentation, so you're left to figure out what the instructions mean on your own.

It seems like the assembly is meant to operate on a set of registers that are each named with a single letter and that can each hold a single integer. You suppose each register should start with a value of 0.

There aren't that many instructions, so it shouldn't be hard to figure out what they do. Here's what you determine:

snd X plays a sound with a frequency equal to the value of X.
set X Y sets register X to the value of Y.
add X Y increases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
Many of the instructions can take either a register (a single letter) or a number. The value of a register is the integer it contains; the value of a number is that number.

After each jump instruction, the program continues with the instruction to which the jump jumped. After any other instruction, the program continues with the next instruction. Continuing (or jumping) off either end of the program terminates it.

For example:

set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
The first four instructions set a to 1, add 2 to it, square it, and then set it to itself modulo 5, resulting in a value of 4.
Then, a sound with frequency 4 (the value of a) is played.
After that, a is set to 0, causing the subsequent rcv and jgz instructions to both be skipped (rcv because a is 0, and jgz because a is not greater than 0).
Finally, a is set to 1, causing the next jgz instruction to activate, jumping back two instructions to another jump, which jumps again to the rcv, which ultimately triggers the recover operation.
At the time the recover operation is executed, the frequency of the last sound played is 4.

What is the value of the recovered frequency (the value of the most recently played sound) the first time a rcv instruction is executed with a non-zero value?

--- Part Two ---
As you congratulate yourself for a job well done, you notice that the documentation has been on the back of the tablet this entire time. While you actually got most of the instructions correct, there are a few key differences. This assembly code isn't about sound at all - it's meant to be run twice at the same time.

Each running copy of the program has its own set of registers and follows the code independently - in fact, the programs don't even necessarily run at the same speed. To coordinate, they use the send (snd) and receive (rcv) instructions:

snd X sends the value of X to the other program. These values wait in a queue until that program is ready to receive them. Each program has its own message queue, so a program can never receive a message it sent.
rcv X receives the next value and stores it in register X. If no values are in the queue, the program waits for a value to be sent to it. Programs do not continue to the next instruction until they have received a value. Values are received in the order they are sent.
Each program also has its own program ID (one 0 and the other 1); the register p should begin with this value.

For example:

snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
Both programs begin by sending three values to the other. Program 0 sends 1, 2, 0; program 1 sends 1, 2, 1. Then, each program receives a value (both 1) and stores it in a, receives another value (both 2) and stores it in b, and then each receives the program ID of the other program (program 0 receives 1; program 1 receives 0) and stores it in c. Each program now sees a different value in its own copy of register c.

Finally, both programs try to rcv a fourth time, but no data is waiting for either of them, and they reach a deadlock. When this happens, both programs terminate.

It should be noted that it would be equally valid for the programs to run at different speeds; for example, program 0 might have sent all three values and then stopped at the first rcv before program 1 executed even its first instruction.

Once both of your programs have terminated (regardless of what caused them to do so), how many times did program 1 send a value?

"""
from collections import defaultdict
import queue
import threading


class Interpreter:
    COMMANDS = {
        'snd': 'sound',
        'set': 'set_register',
        'add': 'add_register',
        'mul': 'mul_register',
        'mod': 'mod_register',
        'rcv': 'recover',
        'jgz': 'jump',
    }

    def __init__(self):
        self.registers = defaultdict(int)
        self.stack = []
        self.current = 0
        self.recovered = None

    def run(self, instructions):
        self.instructions = instructions
        while True:
            if self.current < 0 or self.current >= len(self.instructions):
                return
            instruction_code, args = self.instructions[self.current]
            command_name = self.COMMANDS[instruction_code]
            command = getattr(self, command_name)
            command(*args)
            if self.recovered:
                break
            if command != self.jump:
                self.current += 1

    def _value(self, x):
        if isinstance(x, str):
            return self.registers[x]
        return x

    def sound(self, x):
        x = self._value(x)
        self.stack.append(x)
        return x

    def set_register(self, x, y):
        y = self._value(y)
        self.registers[x] = y

    def add_register(self, x, y):
        y = self._value(y)
        self.registers[x] += y

    def mul_register(self, x, y):
        y = self._value(y)
        self.registers[x] *= y

    def mod_register(self, x, y):
        y = self._value(y)
        self.registers[x] %= y

    def recover(self, x):
        x = self._value(x)
        if x != 0:
            value = self.stack[-1]
            self.recovered = value
            return value

    def jump(self, x, y):
        x = self._value(x)
        y = self._value(y)
        if x > 0:
            self.current += y
        else:
            self.current += 1

    def get_recovered(self):
        if self.recovered:
            return self.recovered

class CooperativeInterpreter(Interpreter):
    COMMANDS = Interpreter.COMMANDS.copy()
    COMMANDS.update({'snd': 'send',
                     'rcv': 'receive',})

    def __init__(self, _id, in_queue, out_queue):
        self.id = _id
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.registers = defaultdict(int)
        self.registers['p'] = self.id

    def run(self, instructions):
        self.instructions = instructions
        self.current = 0
        while True:
            if not self.is_index_valid():
                break
            instruction_code, args = self.instructions[self.current]
            command_name = self.COMMANDS[instruction_code]
            command = getattr(self, command_name)
            try:
                command(*args)
            except queue.Empty:
                break
            if command != self.jump:
                self.current += 1

    def is_index_valid(self):
        return 0 <= self.current < len(self.instructions)

    def send(self, x):
        self.registers['send_count'] += 1
        x = self._value(x)
        self.out_queue.put(x)

    def receive(self, x):
        value = self.in_queue.get(timeout=1)
        self.set_register(x, value)

    def get_send_count(self):
        return self.registers['send_count']


def read_input(filename):
    with open(filename) as f:
        instructions = [parse(line.strip()) for line in f]
    return instructions

def parse(line):
    command, *args = line.split(' ')
    for index, arg in enumerate(args):
        try:
            args[index] = int(arg)
        except ValueError:
            continue
    return command, tuple(args)

def main():
    instructions = read_input('input18.txt')

    interpreter = Interpreter()
    interpreter.run(instructions)
    result = interpreter.get_recovered()
    print('Part 1 solution:', result)

    queue_0 = queue.Queue()
    queue_1 = queue.Queue()

    program_0 = CooperativeInterpreter(_id=0, in_queue=queue_0, out_queue=queue_1)
    program_1 = CooperativeInterpreter(_id=1, in_queue=queue_1, out_queue=queue_0)

    thread_0 = threading.Thread(target=program_0.run, args=(instructions,))
    thread_1 = threading.Thread(target=program_1.run, args=(instructions,))

    thread_0.start()
    thread_1.start()

    thread_0.join()
    thread_1.join()

    result = program_1.get_send_count()
    print('Part 2 solution:', result)


if __name__ == '__main__':
    main()
