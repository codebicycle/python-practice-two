"""
--- Day 11: Hex Ed ---
Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).

"""
import math

DIRECTIONS = {
    'n':  ( 0,  2),
    'ne': ( 2,  1),
    'se': ( 2, -1),
    's':  ( 0, -2),
    'sw': (-2, -1),
    'nw': (-2,  1)
}
VECTORS = {value: key for key, value in DIRECTIONS.items()}

def destination(path):
    vectors = convert_to_vector(path)
    finish = add_tuples(*vectors)
    return finish

def distance(point):
    x, y = map(abs, point)
    dx = x / 2
    dy = max(0, (y - dx) / 2)
    return int(dx + dy)

def convert_to_vector(path):
    return [DIRECTIONS[d] for d in path]

def add_tuples(*tuples):
    return tuple(map(sum, zip(*tuples)))

def read_input(filename):
    with open(filename) as f:
        path = [direction.strip() for direction in f.read().split(',')]
    return path

def main():
    path = read_input('input11.txt')
    finish = destination(path)
    result = distance(finish)
    print('Part 1 solution:', result)

    # result =
    # print('Part 2 solution:', result)


if __name__ == '__main__':
    main()

