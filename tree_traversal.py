#!/usr/bin/env python

"""
            a
    b               c
d       e               f

"""
import collections


def dfs(tree):
    """Pre-order tree traversal"""
    stack = [tree[0]]
    output = []
    while stack:
        value, children = stack.pop()
        output.append(value)
        stack.extend(reversed(children))
    return output


def bfs(tree):
    queue = collections.deque([tree[0]])
    output = []
    while queue:
        value, children = queue.popleft()
        output.append(value)
        queue.extend(children)
    return output



def main():
    tree = [('a', [('b', [('d', []),
                          ('e', [])]),
                   ('c', [('f', [])])])]


    depth_first_search = dfs(tree)
    print('Depth First Search:', depth_first_search)


    breadth_first_search = bfs(tree)
    print('Breadth First Search:', breadth_first_search)


if __name__ == '__main__':
    main()
