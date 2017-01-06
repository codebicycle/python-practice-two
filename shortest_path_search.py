FAIL = []


def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set()
    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                newpath = path + [action, state]
                if is_goal(state):
                    return newpath
                else:
                    frontier.append(newpath)
    return FAIL


# --------------
# Example problem
#
# Let's say the states in an optimization problem are given by integers.
# From a state, i, the only possible successors are i+1 and i-1. Given
# a starting integer, find the shortest path to the integer 8.
#
# This is an overly simple example of when we can use the
# shortest_path_search function. We just need to define the appropriate
# is_goal and successors functions.

def is_goal_integers(state):
    if state == 8:
        return True
    else:
        return False


def successors_integers(state):
    successors = {state + 1: '->',
                  state - 1: '<-'}
    return successors


def is_goal_pouring(state):
    goal = 6
    X, Y, x, y = state
    return x == goal or y == goal


def successors_pouring(state):
    X, Y, x, y = state
    successors = {
        (X, Y, 0, y): 'Empty X',
        (X, Y, x, 0): 'Empty Y',
        (X, Y, X, y): 'Fill X',
        (X, Y, x, Y): 'Fill Y',
        ((X, Y, x + y, 0) if X >= x + y else (X, Y, X, (x + y) - X)): 'Y -> X',
        ((X, Y, 0, x + y) if Y >= x + y else (X, Y, (x + y) - Y, Y)): 'X -> Y',
    }
    return successors


def main():
    # Test Integers
    assert shortest_path_search(5,
                                successors=successors_integers,
                                is_goal=is_goal_integers) == [5, '->', 6, '->',
                                                              7, '->', 8]

    # Pouring Problem
    path = shortest_path_search((9, 4, 0, 0),
                                successors=successors_pouring,
                                is_goal=is_goal_pouring)
    print(path)


if __name__ == '__main__':
    main()
