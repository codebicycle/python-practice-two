"""
--- Day 13: A Maze of Twisty Little Cubicles ---

You arrive at the first floor of this new building to discover a much less welcoming environment than the shiny atrium of the last one. Instead, you are in a maze of twisty little cubicles, all alike.

Every location in this area is addressed by a pair of non-negative integers (x,y). Each such coordinate is either a wall or an open space. You can't move diagonally. The cube maze starts at 0,0 and seems to extend infinitely toward positive x and y; negative values are invalid, as they represent a location outside the building. You are in a small waiting area at 1,1.

While it seems chaotic, a nearby morale-boosting poster explains, the layout is actually quite logical. You can determine whether a given x,y coordinate will be a wall or an open space using a simple system:

Find x*x + 3*x + 2*x*y + y + y*y.
Add the office designer's favorite number (your puzzle input).
Find the binary representation of that sum; count the number of bits that are 1.
If the number of bits that are 1 is even, it's an open space.
If the number of bits that are 1 is odd, it's a wall.
For example, if the office designer's favorite number were 10, drawing walls as # and open spaces as ., the corner of the building containing 0,0 would look like this:

  0123456789
0 .#.####.##
1 ..#..#...#
2 #....##...
3 ###.#.###.
4 .##..#..#.
5 ..##....#.
6 #...##.###
Now, suppose you wanted to reach 7,4. The shortest route you could take is marked as O:

  0123456789
0 .#.####.##
1 .O#..#...#
2 #OOO.##...
3 ###O#.###.
4 .##OO#OO#.
5 ..##OOO.#.
6 #...##.###
Thus, reaching 7,4 would take a minimum of 11 steps (starting from your current location, 1,1).

What is the fewest number of steps required for you to reach 31,39?

Your puzzle input is 1362.

--- Part Two ---

How many locations (distinct x,y coordinates, including your starting location) can you reach in at most 50 steps?

"""

FAIL = []


def is_goal_closure(goal):
    def is_goal(cell):
        return cell == goal
    return is_goal


def is_odd(number):
    return number % 2 == 1


def successors(cell):
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    successors = []
    for delta in deltas:
        new_x = cell.x + delta[0]
        if new_x < 0:
            continue
        new_y = cell.y + delta[1]
        if new_y < 0:
            continue
        new_cell = Cell(new_x, new_y)
        if not new_cell.is_wall():
            successors.append(new_cell)
    return successors


def search_path(start, successors, is_goal):
    if is_goal(start):
        return [start]
    explored = set()
    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        current_cell = path[-1]
        for cell in successors(current_cell):
            if cell not in explored:
                explored.add(cell)
                newpath = path + [cell]
                if is_goal(cell):
                    return newpath
                else:
                    frontier.append(newpath)
    return FAIL


def reachable(start, successors, max_steps):
    explored = {start}
    frontier = [[start]]
    steps = 0
    while frontier and steps < max_steps:
        steps += 1
        ring = frontier.pop(0)
        newring = []
        for current_cell in ring:
            for newcell in successors(current_cell):
                if newcell not in explored:
                    explored.add(newcell)
                    newring.append(newcell)
        frontier.append(newring)
    return explored


class Cell:
    puzzle_input = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_wall(self):
        decimal = (self.x * self.x + 3 * self.x + 2 * self.x * self.y +
                   self.y + self.y * self.y)
        decimal += self.puzzle_input
        binary = '{0:b}'.format(decimal)
        ones = binary.count('1')
        return is_odd(ones)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def main():
    Cell.puzzle_input = 1362
    start = Cell(1, 1)

    goal = Cell(31, 39)
    is_goal = is_goal_closure(goal)

    path = search_path(start, successors, is_goal)
    length = len(path) - 1

    print(path)
    print('Length:', length)
    print()

    max_steps = 50
    explored = reachable(start, successors, max_steps)
    nr_locations = len(explored)
    print(explored)
    print('Reachable locations: {} ({} steps)'.format(nr_locations, max_steps))


if __name__ == '__main__':
    main()
