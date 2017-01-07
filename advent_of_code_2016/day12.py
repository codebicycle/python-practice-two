""""
--- Day 12: Leonardo's Monorail ---

You finally reach the top floor of this building: a garden with a slanted glass ceiling. Looks like there are no more stars to be had.

While sitting on a nearby bench amidst some tiger lilies, you manage to decrypt some of the files you extracted from the servers downstairs.

According to these documents, Easter Bunny HQ isn't just this building - it's a collection of buildings in the nearby area. They're all connected by a local monorail, and there's another building not far from here! Unfortunately, being night, the monorail is currently not operating.

You remotely connect to the monorail control systems and discover that the boot sequence expects a password. The password-checking logic (your puzzle input) is easy to extract, but the code it uses is strange: it's assembunny code designed for the new computer you just assembled. You'll have to execute the code and get the password.

The assembunny code you've extracted operates on four registers (a, b, c, and d) that start at 0 and can hold any integer. However, it seems to make use of only a few instructions:

    cpy x y copies x (either an integer or the value of a register) into register y.
    inc x increases the value of register x by one.
    dec x decreases the value of register x by one.
    jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.

The jnz instruction moves relative to itself: an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.

For example:

cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a

The above code would set register a to 41, increase its value by 2, decrease its value by 1, and then skip the last dec a (because a is not zero, so the jnz a 2 skips it), leaving register a at 42. When you move past the last instruction, the program halts.

After executing the assembunny code in your puzzle input, what value is left in register a?

"""
import re

RE = re.compile(r'(?P<instruction>\w+) (?P<one>\w+) ?(?P<two>[\w+-]+)?')


def follow_instructions(lines, registers):
    line_nr = 0
    while True:
        delta = 1
        match = RE.match(lines[line_nr])
        assert match
        instruction = match.group('instruction')
        arg_one = match.group('one')
        arg_two = match.group('two')
        if instruction == 'cpy':
            registers[arg_two] = value(arg_one, registers)
        elif instruction == 'inc':
            registers[arg_one] += 1
        elif instruction == 'dec':
            registers[arg_one] -= 1
        elif instruction == 'jnz':
            if value(arg_one, registers) != 0:
                delta = int(arg_two)

        line_nr += delta

        if line_nr < 0:
            line_nr = 0
        elif line_nr >= len(lines):
            break


def value(arg, registers):
    try:
        value = int(arg)
    except ValueError:
        return registers[arg]
    return value


def main():
    with open('input12.txt', 'r') as f:
        lines = f.readlines()

    registers = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
    }

    follow_instructions(lines, registers)
    print(registers)

if __name__ == '__main__':
    main()
