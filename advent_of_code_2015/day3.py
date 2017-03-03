"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

"""
import collections


def vector_addition(a_tuple, b_tuple):
    return tuple(x + y for x, y in zip(a_tuple, b_tuple))


class Santa:
    DIRECTIONS = {
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0),
    }

    def __init__(self, start=(0, 0)):
        self.location = start
        self.visited = collections.defaultdict(int)
        self.visited[start] += 1

    def move(self, direction):
        direction_vector = self.DIRECTIONS[direction]
        new_location = vector_addition(self.location, direction_vector)
        self.location = new_location
        self.visited[self.location] += 1

    def count_visited(self):
        return len(self.visited)


def main():
    with open('input3.txt', 'r') as f:
        directions = f.read().strip()

    santa = Santa()
    for arrow in directions:
        santa.move(arrow)

    houses_visited = santa.count_visited()
    print('{} houses visited.'.format(houses_visited))


if __name__ == '__main__':
    main()
