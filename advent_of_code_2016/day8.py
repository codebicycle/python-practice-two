"""
--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

    rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
    rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
    rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.

For example, here is a simple sequence on a smaller screen:

    rect 3x2 creates a small rectangle in the top-left corner:

    ###....
    ###....
    .......

    rotate column x=1 by 1 rotates the second column down by one pixel:

    #.#....
    ###....
    .#.....

    rotate row y=0 by 4 rotates the top row right by four pixels:

    ....#.#
    ###....
    .#.....

    rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

    .#..#.#
    #.#....
    .#.....

As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?

--- Part Two ---

You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?

"""
import collections
import re

RECT = re.compile(r'rect.*?(\d+).*?(\d+)')
ROTATE_ROW = re.compile(r'rotate row.*?(\d+).*?(\d+)')
ROTATE_COLUMN = re.compile(r'rotate column.*?(\d+).*?(\d+)')


def transpose_deque(matrix):
    transposed_tuples = zip(*matrix)
    transposed = [collections.deque(tup) for tup in transposed_tuples]
    return transposed


class Screen:
    OFF = '.'
    ON = '#'

    def __init__(self, width, height):
        self.columns = width
        self.rows = height
        self.screen = []
        for _ in range(self.rows):
            row = collections.deque(self.OFF) * self.columns
            self.screen.append(row)

    def __str__(self):
        lines = []
        for row in self.screen:
            line = ''.join(row)
            lines.append(line)
        return '\n'.join(lines) + '\n'

    def rectangle(self, width, height):
        for row in range(height):
            for col in range(width):
                self.screen[row][col] = self.ON

    def rotate_row(self, index, amount):
        self.screen[index].rotate(amount)

    def rotate_column(self, index, amount):
        transposed = transpose_deque(self.screen)
        transposed[index].rotate(amount)
        self.screen = transpose_deque(transposed)

    def count_lit_pixels(self):
        total = 0
        for row in self.screen:
            total += row.count(self.ON)
        return total


def is_rect(line, screen):
    match = RECT.match(line)
    if match:
        width = int(match.group(1))
        height = int(match.group(2))
        screen.rectangle(width, height)
        return True
    return False


def is_rotate_row(line, screen):
    match = ROTATE_ROW.match(line)
    if match:
        index = int(match.group(1))
        amount = int(match.group(2))
        screen.rotate_row(index, amount)
        return True
    return False


def is_rotate_column(line, screen):
    match = ROTATE_COLUMN.match(line)
    if match:
        index = int(match.group(1))
        amount = int(match.group(2))
        screen.rotate_column(index, amount)
        return True
    return False


def main():
    # screen = Screen(7, 3)
    # screen.rectangle(3, 2)
    # print(screen)
    # screen.rotate_column(1, 1)
    # print(screen)
    # screen.rotate_row(0, 4)
    # print(screen)
    # screen.rotate_column(1, 1)

    # print(screen)
    # print(screen.count_lit_pixels())

    with open('input8.txt', 'r') as f:
        lines = f.readlines()

    screen = Screen(50, 6)

    for line in lines:
        if (is_rect(line, screen) or
                is_rotate_row(line, screen) or
                is_rotate_column(line, screen)):
            print(line)
            print(screen)
            pass

    # print(screen)
    print(screen.count_lit_pixels())


if __name__ == '__main__':
    main()
