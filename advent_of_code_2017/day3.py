"""
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

Your puzzle input is 368078.

"""

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def distance_to_center(value):
    previous_largest = 1
    for ring_number in range(value):
        ring_largest_value = ring_size(ring_number) + previous_largest
        if ring_largest_value >= value:
            break
        previous_largest = ring_largest_value
    log.debug(f'Ring {ring_number}, largest value {ring_largest_value}, '
              f'previous largest {previous_largest}.')

    middles = ring_sides_middles(ring_number, ring_largest_value)
    distance_to_middle = distance_to_closest_middle(value, middles)

    return ring_number + distance_to_middle

def ring_size(ring_number):
    return 8 * ring_number

def ring_side_length(ring_number):
    return 2 * ring_number + 1

def ring_sides_middles(ring_number, largest_value):
    """Ring middles in clockwise order, from largest to smallest"""
    side_length = ring_side_length(ring_number)
    south = largest_value - side_length // 2
    west = south - (side_length - 1)
    north = west - (side_length - 1)
    east = north - (side_length - 1)
    log.debug(f'Ring {ring_number}, Middles: south {south}, '
              f'west {west}, north {north}, east {east}.')
    return south, west, north, east

def distance_to_closest_middle(value, middles):
    distances = [abs(value - middle) for middle in middles]
    return min(distances)

def main():
    puzzle_input = 368078

    result = distance_to_center(puzzle_input)
    print(f'Part 1 solution: {result}')


if __name__ == '__main__':
    main()
