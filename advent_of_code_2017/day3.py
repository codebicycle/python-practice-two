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

--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?

"""
import collections
import itertools
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

# Part 2
NEIGHBOURS = ((-1,  1), (0,  1), (1,  1),
              (-1,  0),          (1,  0),
              (-1, -1), (0, -1), (1, -1))

DIRECTIONS = {
    'north': ( 0,  1),
    'east':  ( 1,  0),
    'south': ( 0, -1),
    'west':  (-1,  0)
}

def populate(target_value):
    squares = collections.defaultdict(int)
    spiral = spiral_generator()
    current = next(spiral)
    value = 1
    squares[current] = value
    while value <= target_value:
        current = next(spiral)
        value = sum_neighbours(current, squares)
        squares[current] = value
    return squares, value


def sum_neighbours(current_position, squares):
    sum = 0
    for vector in NEIGHBOURS:
        neighbour_position = add_points(current_position, vector)
        sum += squares[neighbour_position]
    return sum


def spiral_generator():
    current = (0, 0)
    yield current
    counter = itertools.count(start=1)
    for ring_number in counter:
        side_length = ring_side_length(ring_number)
        current = east(current)
        yield current
        for i in range(side_length - 2):
            current = north(current)
            yield current
        for i in range(side_length - 1):
            current = west(current)
            yield current
        for i in range(side_length - 1):
            current = south(current)
            yield current
        for i in range(side_length -1):
            current = east(current)
            yield current

def north(position):
    return add_points(position, DIRECTIONS['north'])

def east(position):
    return add_points(position, DIRECTIONS['east'])

def south(position):
    return add_points(position, DIRECTIONS['south'])

def west(position):
    return add_points(position, DIRECTIONS['west'])

def add_points(a, b):
    return tuple(map(sum, zip(a, b)))

def main():
    puzzle_input = 368078

    result = distance_to_center(puzzle_input)
    print(f'Part 1 solution: {result}')

    _, result = populate(puzzle_input)
    print(f'Part 2 solution: {result}')

if __name__ == '__main__':
    main()
