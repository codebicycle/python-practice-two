import collections
from pprint import pprint

WALL = '#'
OPEN = '.'

Cell = collections.namedtuple('Cell', 'x, y')


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
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    successors = []
    for delta in deltas:
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


def main():
    maze_str = """
    ..#.
    ..#.
    .#..
    ...#
    """

    maze = parse(maze_str)
    pprint(maze)

if __name__ == '__main__':
    main()
