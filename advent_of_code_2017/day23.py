"""
--- Day 23: Coprocessor Conflagration ---
You decide to head directly to the CPU and fix the printer from there. As you get close, you find an experimental coprocessor doing so much work that the local programs are afraid it will halt and catch fire. This would cause serious issues for the rest of the computer, so you head in and see what you can do.

The code it's running seems to be a variant of the kind you saw recently on that tablet. The general functionality seems very similar, but some of the instructions are different:

set X Y sets register X to the value of Y.
sub X Y decreases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
Only the instructions listed above are used. The eight registers here, named a through h, all start at 0.

The coprocessor is currently set to some kind of debug mode, which allows for testing, but prevents it from doing any meaningful work.

If you run the program (your puzzle input), how many times is the mul instruction invoked?

"""


class BaseInterpreter:
    COMMANDS = {'label': 'method'}

    def __init__(self):
        self.registers = {}

    def _value(self, x):
        if isinstance(x, str):
            return self.registers[x]
        return x

    def run(self, instructions):
        self.instructions = instructions
        self.current = 0

    def _is_index_valid(self):
        return  0 <= self.current < len(self.instructions)

    def _get_method(self):
        label, args = self.instructions[self.current]
        command_name = self.COMMANDS[label]
        method = getattr(self, command_name)
        return method, args


class ExperimentalCoprocessor(BaseInterpreter):
    COMMANDS = {
        'set': 'set_register',
        'sub': 'sub_register',
        'mul': 'mul_register',
        'jnz': 'jump',
    }

    def __init__(self):
        self.registers = dict.fromkeys('abcdefgh', 0)
        self.mul_count = 0

    def run(self, instructions):
        self.instructions = instructions
        self.current = 0
        while self._is_index_valid():
            method, args = self._get_method()
            method(*args)

            if method != self.jump:
                self.current += 1

    def set_register(self, x, y):
        y = self._value(y)
        self.registers[x] = y

    def sub_register(self, x, y):
        y = self._value(y)
        self.registers[x] -= y

    def mul_register(self, x, y):
        self.mul_count += 1
        y = self._value(y)
        self.registers[x] *= y

    def jump(self, x, y):
        x = self._value(x)
        y = self._value(y)
        if x != 0:
            self.current += y
        else:
            self.current += 1


class InstructionParser():
    @staticmethod
    def parse(lines):
        instructions = []
        for line in lines:
            command, *args = line.strip().split(' ')
            for index, arg in enumerate(args):
                try:
                    args[index] = int(arg)
                except ValueError:
                    continue
            instruction = command, tuple(args)
            instructions.append(instruction)
        return instructions


def read_input(filename):
    with open(filename) as f:
        puzzle_input = f.readlines()
    return puzzle_input

def main():
    puzzle_input = read_input('input23.txt')
    instructions = InstructionParser.parse(puzzle_input)

    cpu = ExperimentalCoprocessor()
    cpu.run(instructions)

    result = cpu.mul_count
    print('Part 1 solution:', result)

    # result =
    # print('Part 2 solution:', result)


if __name__ == '__main__':
    main()

