"""
--- Day 19: A Series of Tubes ---
Somehow, a network packet got lost and ended up here. It's trying to follow a routing diagram (your puzzle input), but it's confused about where to go.

Its starting point is just off the top of the diagram. Lines (drawn with |, -, and +) show the path it needs to take, starting by going down onto the only line connected to the top of the diagram. It needs to follow this path until it reaches the end (located somewhere within the diagram) and stop there.

Sometimes, the lines cross over each other; in these cases, it needs to continue going the same direction, and only turn left or right when there's no other option. In addition, someone has left letters on the line; these also don't change its direction, but it can use them to keep track of where it's been. For example:

     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+

Given this diagram, the packet needs to take the following path:

Starting at the only line touching the top of the diagram, it must go down, pass through A, and continue onward to the first +.
Travel right, up, and right, passing through B in the process.
Continue down (collecting C), right, and up (collecting D).
Finally, go all the way left through E and stopping at F.
Following the path to the end, the letters it sees on its path are ABCDEF.

The little packet looks up at you, hoping you can help it find the way. What letters will it see (in the order it would see them) if it follows the path? (The routing diagram is very wide; make sure you view it without line wrapping.)

--- Part Two ---
The packet is curious how many steps it needs to go.

For example, using the same routing diagram from the example above...

     |
     |  +--+
     A  |  C
 F---|--|-E---+
     |  |  |  D
     +B-+  +--+

...the packet would go:

6 steps down (including the first line at the top of the diagram).
3 steps right.
4 steps up.
3 steps right.
4 steps down.
3 steps right.
2 steps up.
13 steps left (including the F it stops on).
This would result in a total of 38 steps.

How many steps does the packet need to go?

"""
from collections import namedtuple
import string
import logging


class Maze:
    """Grid origin: top left corner"""
    NORTH = ( 0, -1)
    SOUTH = ( 0,  1)
    EAST =  ( 1,  0)
    WEST =  (-1,  0)
    VERTICAL = {NORTH, SOUTH}
    HORIZONTAL = {EAST, WEST}
    DIRECTIONS = VERTICAL.union(HORIZONTAL)
    LETTERS = set(string.ascii_uppercase)

    def __init__(self, maze):
        self.maze = maze
        self.current_position = self._start_position()
        self.letters = []
        self.steps_count = 0

    def __str__(self):
        lines = [''.join(row) for row in self.maze]
        return '\n'.join(lines)

    def _start_position(self):
        y = 0
        x = self.maze[y].index('|')
        return x, y

    def _change_direction(self, previous_direction=None):
        if previous_direction is None:
            return self.SOUTH
        elif previous_direction in self.VERTICAL:
            remaining_directions = self.HORIZONTAL
        else:
            remaining_directions = self.VERTICAL

        for direction in remaining_directions:
            x, y = add_tuples(direction, self.current_position)
            candidate = self.maze[y][x]
            if candidate in '|-':
                return direction

    def _move_straight(self, direction):
        self._move(direction)
        current_value = self.current_value()
        if current_value == ' ':
            raise ValueError('Maze finished or stepped outside.')

        if current_value != '+':
            self._collect(current_value)
            self._move_straight(direction)

    def _move(self, direction):
        self.steps_count += 1
        self.current_position = add_tuples(self.current_position, direction)

    def traverse(self):
        previous_direction = None
        while True:
            direction = self._change_direction(previous_direction)
            try:
                self._move_straight(direction)
            except ValueError:
                break
            previous_direction = direction

    def current_value(self):
        x, y = self.current_position
        return self.maze[y][x]

    def _collect(self, value):
        if value in self.LETTERS:
            self.letters.append(value)


def add_tuples(*tuples):
   return tuple(map(sum, zip(*tuples)))

def read_input(filename):
    with open(filename) as f:
        maze = [[char for char in line.rstrip('\r\n')]
                for line in f]
    return maze

def main():
    puzzle_input = read_input('input19.txt')

    maze = Maze(maze=puzzle_input)
    maze.traverse()

    result = ''.join(maze.letters)
    print('Part 1 solution:', result)

    result = maze.steps_count
    print('Part 2 solution:', result)


if __name__ == '__main__':
    main()

