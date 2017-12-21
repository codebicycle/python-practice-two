"""
--- Day 14: Disk Defragmentation ---
Suddenly, a scheduled job activates the system's disk defragmenter. Were the situation different, you might sit and watch it for a while, but today, you just don't have that kind of time. It's soaking up valuable system resources that are needed elsewhere, and so the only option is to help it finish its task as soon as possible.

The disk in question consists of a 128x128 grid; each square of the grid is either free or used. On this disk, the state of the grid is tracked by the bits in a sequence of knot hashes.

A total of 128 knot hashes are calculated, each corresponding to a single row in the grid; each hash contains 128 bits which correspond to individual grid squares. Each bit of a hash indicates whether that square is free (0) or used (1).

The hash inputs are a key string (your puzzle input), a dash, and a number from 0 to 127 corresponding to the row. For example, if your key string were flqrgnkx, then the first row would be given by the bits of the knot hash of flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and so on until the last row, flqrgnkx-127.

The output of a knot hash is traditionally represented by 32 hexadecimal digits; each of these digits correspond to 4 bits, for a total of 4 * 32 = 128 bits. To convert to bits, turn each hexadecimal digit to its equivalent binary value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110, f becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal would begin with 10100000110000100000000101110000... in binary.

Continuing this process, the first 8 rows and columns for key flqrgnkx appear as follows, using # to denote used squares, and . to denote free ones:

##.#.#..-->
.#.#.#.#
....#.#.
#.#.##.#
.##.#...
##..#..#
.#...#..
##.#.##.-->
|      |
V      V
In this example, 8108 squares are used across the entire 128x128 grid.

Given your actual key string, how many squares are used?

"""
from day10 import knot_hash


class GridBuilder:
    def build(self, key):
        state = []
        for i in range(128):
            row_key = f'{key}-{i}'
            row_hash = knot_hash(row_key)
            row = self._to_binary(row_hash)
            state.append(list(row))

        return Grid(state)

    def _to_binary(self, hex_string):
        accumulator = []
        for char in hex_string:
            x = int(char, 16)
            accumulator.append(f'{x:04b}')
        return ''.join(accumulator)


class Grid:
    def __init__(self, state):
        self.state = state

    def count_used(self):
        return sum(row.count('1') for row in self.state)

    def __str__(self):
        alternative = [['.' if char == '0' else '#' for char in row]
                       for row in self.state]
        return '\n'.join(''.join(row) for row in alternative)

def read_input(filename):
    with open(filename) as f:
        puzzle_input = f.read().strip()

    return puzzle_input

def main():
    puzzle_input = read_input('input14.txt')

    grid = GridBuilder().build(key=puzzle_input)
    result = grid.count_used()
    print('Part 1 solution:', result)

    # result =
    # print('Part 2 solution:', result)


if __name__ == '__main__':
    main()
