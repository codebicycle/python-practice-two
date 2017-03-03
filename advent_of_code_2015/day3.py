"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

"""
import collections
import itertools


def vector_addition(a_tuple, b_tuple):
    return tuple(x + y for x, y in zip(a_tuple, b_tuple))


class Santa:
    DIRECTIONS = {
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0),
    }

    visited = collections.defaultdict(int)

    def __init__(self, start=(0, 0)):
        self.location = start
        self.visited[start] += 1

    def move(self, direction):
        direction_vector = self.DIRECTIONS[direction]
        new_location = vector_addition(self.location, direction_vector)
        self.location = new_location
        self.visited[self.location] += 1

    @classmethod
    def count_visited(cls):
        return len(cls.visited)

    @classmethod
    def reset_visited(cls):
        cls.visited.clear()


def deliver_presents(num_workers, directions):
    workers = [Santa() for _ in range(num_workers)]
    workers_iterator = itertools.cycle(workers)

    for arrow in directions:
        next(workers_iterator).move(arrow)

    return Santa.count_visited()


def main():
    with open('input3.txt', 'r') as f:
        directions = f.read().strip()

    houses_one_santa = deliver_presents(1, directions)
    print('Santa visited {} houses.'.format(houses_one_santa))
    print()

    Santa.reset_visited()
    houses_two_santas = deliver_presents(2, directions)
    print('Santa and Robo-Santa visited {} houses.'.format(houses_two_santas))


if __name__ == '__main__':
    main()
