"""
All Pairs Shortest Path

Use Dynammic Programming to determine the shortest accumulated totat of a path
between any two vertices in a weighted graph.

The code uses a graph representation such as the following:

graph = {
    0: {1: 2, 4: 4},
    1: {2: 3},
    2: {3: 5, 4: 1},
    3: {0: 8},
    4: {3: 3},
}

A dictionary where keys are the vertices and the values are
dicts of vertex: weight pairs.
"""

from pprint import pprint

def build_matrices(graph):
    """Build adjacency matrix and predecessors matrix"""
    adjacency = {}
    predecessors = {}
    for v1 in graph:
        for v2 in graph:
            if v1 == v2:
                cost = 0
                predecessor = None
            elif v2 in graph[v1]:
                cost = graph[v1][v2]
                predecessor = v1
            else:
                cost = float('inf')
                predecessor = None
            adjacency[v1, v2] = cost
            predecessors[v1, v2] = predecessor
    return adjacency, predecessors

def shortest_path(graph, start, finish):
    distance, predecessors = all_pairs_shortest_path(graph)
    path = _build_path(predecessors, start, finish)
    return distance[start, finish], path

def _build_path(predecessors, start, finish):
    path_backwards = []
    predecessor = finish
    while predecessor is not None:
        path_backwards.append(predecessor)
        predecessor = predecessors[start, predecessor]
    return list(reversed(path_backwards))

def all_pairs_shortest_path(graph):
    distance, predecessors = build_matrices(graph)

    for vertex in graph:
        for pair in distance:
            if vertex in pair:
                continue
            v1, v2 = pair
            cost_through_vertex = distance[v1, vertex] + distance[vertex, v2]
            if distance[pair] > cost_through_vertex:
                distance[pair] = cost_through_vertex
                predecessors[pair] = predecessors[vertex, v2]
    return distance, predecessors


def main():
    graph = {
        0: {1: 2, 4: 4},
        1: {2: 3},
        2: {3: 5, 4: 1},
        3: {0: 8},
        4: {3: 3},
    }

    start = 2
    finish = 3
    cost, path = shortest_path(graph, start, finish)
    print(f'The shortest path (lowest cost path) between vertices {start} and {finish} is {path}'
          f' and its cost is {cost}.')


if __name__ == '__main__':
    main()
