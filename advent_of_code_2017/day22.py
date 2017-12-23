"""
--- Day 22: Sporifica Virus ---
Diagnostics indicate that the local grid computing cluster has been contaminated with the Sporifica Virus. The grid computing cluster is a seemingly-infinite two-dimensional grid of compute nodes. Each node is either clean or infected by the virus.

To prevent overloading the nodes (which would render them useless to the virus) or detection by system administrators, exactly one virus carrier moves through the network, infecting or cleaning nodes as it moves. The virus carrier is always located on a single node in the network (the current node) and keeps track of the direction it is facing.

To avoid detection, the virus carrier works in bursts; in each burst, it wakes up, does some work, and goes back to sleep. The following steps are all executed in order one time each burst:

If the current node is infected, it turns to its right. Otherwise, it turns to its left. (Turning is done in-place; the current node does not change.)
If the current node is clean, it becomes infected. Otherwise, it becomes cleaned. (This is done after the node is considered for the purposes of changing direction.)
The virus carrier moves forward one node in the direction it is facing.
Diagnostics have also provided a map of the node infection status (your puzzle input). Clean nodes are shown as .; infected nodes are shown as #. This map only shows the center of the grid; there are many more nodes beyond those shown, but none of them are currently infected.

The virus carrier begins in the middle of the map facing up.

For example, suppose you are given a map like this:

..#
#..
...
Then, the middle of the infinite grid looks like this, with the virus carrier's position marked with [ ]:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . . #[.]. . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
The virus carrier is on a clean node, so it turns left, infects the node, and moves left:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . # . . .
. . .[#]# . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
The virus carrier is on an infected node, so it turns right, cleans the node, and moves up:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . .[.]. # . . .
. . . . # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
Four times in a row, the virus carrier finds a clean, infects it, turns left, and moves forward, ending in the same place and still facing up:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . #[#]. # . . .
. . # # # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
Now on the same node as before, it sees an infection, which causes it to turn right, clean the node, and move forward:

. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . # .[.]# . . .
. . # # # . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
After the above actions, a total of 7 bursts of activity had taken place. Of them, 5 bursts of activity caused an infection.

After a total of 70, the grid looks like this, with the virus carrier facing up:

. . . . . # # . .
. . . . # . . # .
. . . # . . . . #
. . # . #[.]. . #
. . # . # . . # .
. . . . . # # . .
. . . . . . . . .
. . . . . . . . .
By this time, 41 bursts of activity caused an infection (though most of those nodes have since been cleaned).

After a total of 10000 bursts of activity, 5587 bursts will have caused an infection.

Given your actual map, after 10000 bursts of activity, how many bursts cause a node to become infected? (Do not count nodes that begin infected.)

"""

class Grid:
    NORTH = ( 0,  1)
    SOUTH = ( 0, -1)
    EAST =  ( 1,  0)
    WEST =  (-1,  0)
    DIRECTIONS = (NORTH, EAST, SOUTH, WEST)

    def __init__(self):
        self.infected = set()
        self.current = 0, 0
        self.direction = self.NORTH
        self.infections_count = 0

    def parse(self, lines):
        height = len(lines)
        width = len(lines[0])
        initial_x = -1 * (width // 2)
        initial_y = height // 2

        y = initial_y
        for line in lines:
            x = initial_x
            for char in line:
                if char == '#':
                    self.infected.add((x, y))
                x += 1
            y -= 1

    def burst(self):
        if self._is_infected():
            self._turn_right()
            self._clean()
        else:
            self._turn_left()
            self._infect()
        self._move()

    def simulate(self, times):
        for _ in range(times):
            self.burst()

    def _clean(self):
        self.infected.remove(self.current)

    def _infect(self):
        self.infections_count += 1
        self.infected.add(self.current)

    def _is_infected(self):
        return self.current in self.infected

    def _move(self):
        self.current = add_tuples(self.current, self.direction)

    def _turn_left(self):
        current = self.DIRECTIONS.index(self.direction)
        left = current - 1
        self.direction = self.DIRECTIONS[left]

    def _turn_right(self):
        current = self.DIRECTIONS.index(self.direction)
        left = (current + 1) % len(self.DIRECTIONS)
        self.direction = self.DIRECTIONS[left]


def add_tuples(*tuples):
    return tuple(map(sum, zip(*tuples)))

def read_input(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f]
    return lines

def main():
    puzzle_input = read_input('input22.txt')

    grid = Grid()
    grid.parse(puzzle_input)
    grid.simulate(10_000)

    result = grid.infections_count
    print('Part 1 solution:', result)

    # result =
    # print('Part 2 solution:', result)


if __name__ == '__main__':
    main()
