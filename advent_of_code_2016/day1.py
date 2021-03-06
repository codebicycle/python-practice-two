"""
--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolength... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent calengthdar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:

    Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
    R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
    R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?

--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

"""


def add_elements(tuple_a, tuple_b):
    return tuple(a + b for a, b in zip(tuple_a, tuple_b))


def get_first_duplicate(locations):
    no_duplicates = set()
    length = 0
    for location in locations:
        no_duplicates.add(location)
        length += 1
        if len(no_duplicates) != length:
            return location


class Turtle:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    DIRECTION = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def __init__(self):
        self.facing = self.NORTH
        self.location = (0, 0)
        self.path = []

    def move(self, direction, length):
        self.turn(direction)
        vector = self.DIRECTION[self.facing]
        for step in range(length):
            self.location = add_elements(self.location, vector)
            self.path.append(self.location)

    def turn(self, direction):
        if direction == 'l':
            self.facing = (self.facing - 1) % 4
        elif direction == 'r':
            self.facing = (self.facing + 1) % 4
        else:
            raise ValueError(
                "Bad direction {}, expected 'l' or 'r'".format(direction))

    def travel(self, raw_indications):
        indications = prepare(raw_indications)
        for indication in indications:
            direction, length = parse(indication)
            self.move(direction, length)

    def get_distance(self, start=(0, 0), end=None):
        if end is None:
            end = self.location
        x1, y1 = start
        x2, y2 = end
        distance = abs(x2 - x1) + abs(y2 - y1)
        return distance

    def get_distance_first_visit_twice(self):
        first_location_visited_twice = get_first_duplicate(self.path)
        if first_location_visited_twice:
            distance = self.get_distance(end=first_location_visited_twice)
            return distance


def parse(indication):
    direction = indication[0].lower()
    length = int(indication[1:])
    return direction, length


def prepare(raw_indications):
    return [indication.strip()
            for indication in raw_indications.split(',')]


def main():
    with open('input1.txt', 'r') as f:
        raw_indications = f.read()

    turtle = Turtle()
    turtle.travel(raw_indications)

    distance_traveled = turtle.get_distance()
    print(distance_traveled)

    distance_to_first_visit_twice = turtle.get_distance_first_visit_twice()
    print(distance_to_first_visit_twice)


if __name__ == '__main__':
    main()
