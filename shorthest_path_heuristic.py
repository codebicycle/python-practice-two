import collections
from pprint import pprint

WALL = '#'
OPEN = '.'


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def taxicab_distance(start, end):
    """Cells start, end"""
    return abs(start.x - end.x) + abs(start.y - end.y)


def taxicab_heuristic_closure(end):
    def inner(start):
        return taxicab_distance(start, end)
    return inner


def is_goal_closure(goal):
    def is_goal(cell):
        return cell == goal
    return is_goal


def outside(num, len_interval):
    return not 0 <= num < len_interval


def is_open(cell, maze):
    return maze[cell.y][cell.x] == OPEN


def successors(cell, maze):
    len_x = len(maze[0])
    len_y = len(maze)
    # north, east, south, west
    NESW = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    successors = []
    for delta in NESW:
        new_x = cell.x + delta[0]
        if outside(new_x, len_x):
            continue
        new_y = cell.y + delta[1]
        if outside(new_y, len_y):
            continue
        new_cell = Cell(new_x, new_y)
        if is_open(new_cell, maze):
            successors.append(new_cell)
    return successors


def parse(maze_str):
    maze = tuple(tuple(row) for row in maze_str.strip().split())
    return maze


def shortest_path(maze, start, heuristic):
    def is_goal(location):
        return heuristic(location) == 0

    if is_goal(start):
        return [start]
    explored = set()
    frontier = [[start]]
    solutions = []
    while frontier:
        frontier.sort(key=lambda p: heuristic(p[-1]))
        path = frontier.pop(0)
        current_cell = path[-1]
        for cell in successors(current_cell, maze):
            new_path = path + [cell]
            if is_goal(cell):
                solutions.append(new_path)
                print(len(new_path), len(explored), new_path)
            elif cell not in explored:
                explored.add(cell)
                frontier.append(new_path)
    return solutions


def main():
    maze_str = """
    ....
    ..#.
    ..#.
    .#..
    ...#
    """

    maze = parse(maze_str)

    start = Cell(0, 1)
    goal = Cell(3, 0)
    heuristic = taxicab_heuristic_closure(goal)

    paths = shortest_path(maze, start, heuristic=heuristic)

    print('Solutions')
    for path in paths:
        length = len(path)
        print(length, path)

if __name__ == '__main__':
    main()
