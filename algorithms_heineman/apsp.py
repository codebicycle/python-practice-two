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

def build_adjacency_matrix(graph):
    adjacency = {}
    for v1 in graph:
        for v2 in graph:
            if v1 == v2:
                value = 0
            elif v2 in graph[v1]:
                value = graph[v1][v2]
            else:
                value = float('inf')
            adjacency[v1, v2] = value
    return adjacency

def lowest_cost(graph, start, finish):
    distance = all_pairs_lowest_cost(graph)
    return distance[start, finish]

def all_pairs_lowest_cost(graph):
    distance = build_adjacency_matrix(graph)

    for vertex in graph:
        for pair in distance:
            if vertex in pair:
                continue
            v1, v2 = pair
            cost_through_vertex = distance[v1, vertex] + distance[vertex, v2]
            if distance[pair] > cost_through_vertex:
                distance[pair] = cost_through_vertex
    return distance


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
    cost = lowest_cost(graph, start, finish)
    print(f'The lowest cost path between vertex {start} and {finish} has a cost of {cost}.')

if __name__ == '__main__':
    main()
