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

"""
import collections


def turn(facing, direction):
    compass = {
        'n': {'r': 'e',
              'l': 'w'},
        'e': {'r': 's',
              'l': 'n'},
        's': {'r': 'w',
              'l': 'e'},
        'w': {'r': 'n',
              'l': 's'},
    }
    return compass[facing][direction]


def parse(indication):
    direction = indication[0].lower()
    length = int(indication[1:])
    return direction, length


def get_distance(raw_indications):
    orientation = 'n'
    traveled = collections.defaultdict(int)
    indications = [indication.strip()
                   for indication in raw_indications.split(',')]

    for indication in indications:
        direction, length = parse(indication)
        orientation = turn(orientation, direction)
        traveled[orientation] += length

    north = traveled['n']
    east = traveled['e']
    south = traveled['s']
    west = traveled['w']
    distance = abs(north - south) + abs(east - west)
    return distance


def main():
    with open('input1.txt', 'r') as f:
        indications = f.read()

    distance = get_distance(indications)
    print(distance)


if __name__ == '__main__':
    main()
