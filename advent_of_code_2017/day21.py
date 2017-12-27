"""
--- Day 21: Fractal Art ---
You find a program trying to generate some art. It uses a strange process that involves repeatedly enhancing the detail of an image through a set of rules.

The image consists of a two-dimensional square grid of pixels that are either on (#) or off (.). The program always begins with this pattern:

.#.
..#
###
Because the pattern is both 3 pixels wide and 3 pixels tall, it is said to have a size of 3.

Then, the program repeats the following process:

If the size is evenly divisible by 2, break the pixels up into 2x2 squares, and convert each 2x2 square into a 3x3 square by following the corresponding enhancement rule.
Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3 squares, and convert each 3x3 square into a 4x4 square by following the corresponding enhancement rule.
Because each square of pixels is replaced by a larger one, the image gains pixels and so its size increases.

The artist's book of enhancement rules is nearby (your puzzle input); however, it seems to be missing rules. The artist explains that sometimes, one must rotate or flip the input pattern to find a match. (Never rotate or flip the output pattern, though.) Each pattern is written concisely: rows are listed as single units, ordered top-down, and separated by slashes. For example, the following rules correspond to the adjacent patterns:

../.#  =  ..
          .#

                .#.
.#./..#/###  =  ..#
                ###

                        #..#
#..#/..../#..#/.##.  =  ....
                        #..#
                        .##.
When searching for a rule to use, rotate and flip the pattern as necessary. For example, all of the following patterns match the same rule:

.#.   .#.   #..   ###
..#   #..   #.#   ..#
###   ###   ##.   .#.
Suppose the book contained the following two rules:

../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
As before, the program begins with this pattern:

.#.
..#
###
The size of the grid (3) is not divisible by 2, but it is divisible by 3. It divides evenly into a single square; the square matches the second rule, which produces:

#..#
....
....
#..#
The size of this enhanced grid (4) is evenly divisible by 2, so that rule is used. It divides evenly into four squares:

#.|.#
..|..
--+--
..|..
#.|.#
Each of these squares matches the same rule (../.# => ##./#../...), three of which require some flipping and rotation to line up with the rule. The output for the rule is the same in all four cases:

##.|##.
#..|#..
...|...
---+---
##.|##.
#..|#..
...|...
Finally, the squares are joined into a new grid:

##.##.
#..#..
......
##.##.
#..#..
......
Thus, after 2 iterations, the grid contains 12 pixels that are on.

How many pixels stay on after 5 iterations?

"""
class Matrix:
    @classmethod
    def make_variations(cls, matrix):
        variations = []
        current = matrix
        for _ in range(4):
            transposed = cls.transpose(current)
            rotated = cls.flip(transposed)
            variations.append(transposed)
            variations.append(rotated)
            current = rotated
        return variations

    @staticmethod
    def flip(matrix):
        flipped = list(matrix)
        for i in range(len(matrix)):
            flipped[i] = tuple(matrix[i][::-1])
        return tuple(flipped)

    @staticmethod
    def transpose(matrix):
        return tuple(zip(*matrix))

    @classmethod
    def rotate(cls, matrix):
        return cls.flip(cls.transpose(matrix))

    @staticmethod
    def split_matrices(matrix, length=2):
        """Split a square matrix into smaller sqare matrices of the given length
        matrix is a two-dimensional list
        """
        height = len(matrix)
        width = height
        accumulator = []
        for y in range(0, height, length):
            row = []
            for x in range(0, width, length):
                subarray = []
                for i in range(length):
                    subarray.append(matrix[y+i][x:x+length])
                row.append(subarray)
            accumulator.append(row)
        return accumulator


class FractalBuilder:
    OFF = '.'
    ON = '#'
    SEPARATOR = '/'
    INITIAL = '.#./..#/###'

    def _build_rules(self, instructions):
        rules = self._build_rules_from_instructions(instructions)
        self._add_rules_variations(rules)
        return rules

    def _build_rules_from_instructions(self, instructions):
        rules = {}
        for line in instructions:
            rule_str, output_str = line
            rule = self._to_matrix(rule_str)
            output = self._to_matrix(output_str)

            rules[rule] = output
        return rules

    def _add_rules_variations(self, rules):
        """Modifies rules dictionary in place"""
        for rule in rules.copy():
            output = rules[rule]
            variations = Matrix.make_variations(rule)
            for variant in variations:
                if variant in rules:
                    assert rules[variant] == output
                else:
                    rules[variant] = output

    def _to_matrix(self, pattern):
        matrix = []
        row = []
        for char in pattern:
            if char == self.OFF:
                row.append(0)
            elif char == self.ON:
                row.append(1)
            elif char == self.SEPARATOR:
                matrix.append(tuple(row))
                row = []
            else:
                raise ValueError(f'Unexpected character "{char}".')
        matrix.append(tuple(row))
        return tuple(matrix)

    def build(self, instructions):
        rules = self._build_rules(instructions)
        initial_state = self._to_matrix(self.INITIAL)
        return Fractal(rules, initial_state)


class Fractal:
    def __init__(self, rules, initial_state):
        self.rules = rules
        self.state = initial_state

    def iterate(self):
        pass


def read_input(filename):
    with open(filename) as f:
        lines = [line.strip().split(' => ') for line in f]
    return lines

def main():
    puzzle_input = read_input('input21.txt')

    fractal_builder = FractalBuilder()
    fractal = fractal_builder.build(puzzle_input)

    # result =
    # print('Part 1 solution:', result)


    # result =
    # print('Part 2 solution:', result)


if __name__ == '__main__':
    main()
