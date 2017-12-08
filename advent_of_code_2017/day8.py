"""
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?

--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).

"""
import collections
import re


class CPU:
    REGEX = re.compile(r'''(?P<register>\w+) \s
                            (?P<modifier>dec|inc) \s
                            (?P<value>[-\d]+) \s
                            if \s (?P<conditional_register>\w+) \s
                            (?P<conditional_operator>[!=<>]+) \s
                            (?P<conditional_value>[-\d]+)''', re.VERBOSE)

    _registers = collections.defaultdict(int)
    _highest_value = 0

    def _match(self, line):
        match = self.REGEX.match(line)
        return match.groupdict()

    def _compute(self, line):
        groups = self._match(line)
        register = groups['register']
        modifier = groups['modifier']
        value = int(groups['value'])
        conditional_register = groups['conditional_register']
        conditional_operator = groups['conditional_operator']
        conditional_value = groups['conditional_value']

        conditional_register_value = self._registers[conditional_register]
        condition = (f'{conditional_register_value}'
                     f'{conditional_operator}'
                     f'{conditional_value}')
        if eval(condition):
            if modifier == 'inc':
                self._registers[register] += value
            elif modifier == 'dec':
                self._registers[register] -= value
            else:
                raise ValueError(f'Invalid modifier "{modifier}"')

            if self._registers[register] > self._highest_value:
                    self._highest_value = self._registers[register]

    def compute(self, lines):
        for line in lines:
            self._compute(line)

    def current_max_value(self):
        values = self._registers.values()
        return max(values)

    def highest_value(self):
        return self._highest_value


def read_lines(filename):
    with open(filename) as f:
        lines = list(f)
    return lines

def main():
    lines = read_lines('input8.txt')
    cpu = CPU()
    cpu.compute(lines)

    result = cpu.current_max_value()
    print(f'Part 1 solution: {result}')

    result = cpu.highest_value()
    print(f'Part 2 solution: {result}')


if __name__ == '__main__':
    main()
