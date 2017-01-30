"""
--- Day 23: Safe Cracking ---

This is one of the top floors of the nicest tower in EBHQ. The Easter Bunny's private office is here, complete with a safe hidden behind a painting, and who wouldn't hide a star in a safe behind a painting?

The safe has a digital screen and keypad for code entry. A sticky note attached to the safe has a password hint on it: "eggs". The painting is of a large rabbit coloring some eggs. You see 7.

When you go to type the code, though, nothing appears on the display; instead, the keypad comes apart in your hands, apparently having been smashed. Behind it is some kind of socket - one that matches a connector in your prototype computer! You pull apart the smashed keypad and extract the logic circuit, plug it into your computer, and plug your computer into the safe.

Now, you just need to figure out what output the keypad would have sent to the safe. You extract the assembunny code from the logic chip (your puzzle input).

The code looks like it uses almost the same architecture and instruction set that the monorail computer used! You should be able to use the same assembunny interpreter for this as you did there, but with one new instruction:

tgl x toggles the instruction x away (pointing at instructions like jnz does: positive means forward; negative means backward):

    For one-argument instructions, inc becomes dec, and all other one-argument instructions become inc.
    For two-argument instructions, jnz becomes cpy, and all other two-instructions become jnz.
    The arguments of a toggled instruction are not affected.
    If an attempt is made to toggle an instruction outside the program, nothing happens.
    If toggling produces an invalid instruction (like cpy 1 2) and an attempt is later made to execute that instruction, skip it instead.
    If tgl toggles itself (for example, if a is 0, tgl a would target itself and become inc a), the resulting instruction is not executed until the next time it is reached.

For example, given this program:

cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a

    cpy 2 a initializes register a to 2.
    The first tgl a toggles an instruction a (2) away from it, which changes the third tgl a into inc a.
    The second tgl a also modifies an instruction 2 away from it, which changes the cpy 1 a into jnz 1 a.
    The fourth line, which is now inc a, increments a to 3.
    Finally, the fifth line, which is now jnz 1 a, jumps a (3) instructions ahead, skipping the dec a instructions.

In this example, the final value in register a is 3.

The rest of the electronics seem to place the keypad entry (the number of eggs, 7) in register a, run the code, and then send the value left in register a to the safe.

What value should be sent to the safe?

"""
import re

import collections

Command = collections.namedtuple('Command', 'name, arg_one, arg_two')


def parse(lines):
    commands = []
    for line in lines:
        name, arg_one, *arg_two = line.split()
        arg_two = arg_two[0] if arg_two else None

        command = Command(name, arg_one, arg_two)
        commands.append(command)
    return commands


def value(param, registers):
    return registers[param] if param in registers else int(param)


def run_commands(commands, registers):
    # program counter
    pc = 0
    while True:
        delta = 1
        command = commands[pc]
        if command.name == 'cpy':
            if command.arg_two in registers:
                registers[command.arg_two] = value(command.arg_one, registers)
        elif command.name == 'inc':
            registers[command.arg_one] += 1
        elif command.name == 'dec':
            registers[command.arg_one] -= 1
        elif command.name == 'jnz':
            if value(command.arg_one, registers) != 0:
                delta = value(command.arg_two, registers)
        elif command.name == 'tgl':
            target_index = pc + value(command.arg_one, registers)
            if 0 <= target_index < len(commands):
                target = commands[target_index]
                if target.name == 'inc':
                    new_name = 'dec'
                elif target.name in ['dec', 'tgl']:
                    new_name = 'inc'
                elif target.name == 'jnz':
                    new_name = 'cpy'
                elif target.name == 'cpy':
                    new_name = 'jnz'

                new_command = Command(new_name, target.arg_one, target.arg_two)
                commands[target_index] = new_command

        pc += delta
        if pc < 0:
            pc = 0
        elif pc >= len(commands):
            break


def main():
    with open('input23.txt', 'r') as f:
        lines = f.readlines()

    registers = {
        'a': 7,
        'b': 0,
        'c': 0,
        'd': 0,
    }

    commands = parse(lines)
    run_commands(commands, registers)
    print(registers)

if __name__ == '__main__':
    main()
