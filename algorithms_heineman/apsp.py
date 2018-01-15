"""
All Pairs Shortest Path

Use Dynamic Programming to determine the shortest accumulated total of a path
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
dictionaries of vertex: weight pairs.
"""

def shortest_path(graph, start, finish):
    """Return the shortest path and its cost, as a tuple, between the given vertices
    start and finish from the graph.
    """
    distance, predecessors = all_pairs_shortest_path(graph)
    path = _build_path(predecessors, start, finish)
    return path, distance[start, finish]

def all_pairs_shortest_path(graph):
    """Compute the shortest path between all pairs of vertices from the given graph
    Return distance and predecessors as a tuple.
    Distance is a matrix with the costs of the shortest paths.
    Predecessors is a matrix that keeps track of the preceding vertex from the shortest path.
    """
    distance, predecessors = _build_matrices(graph)

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

def _build_matrices(graph):
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

def _build_path(predecessors, start, finish):
    """Construct a path from vertex start to finish given a predecessor matrix"""
    path_backwards = []
    predecessor = finish
    while predecessor is not None:
        path_backwards.append(predecessor)
        predecessor = predecessors[start, predecessor]
    return list(reversed(path_backwards))


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
    path, cost = shortest_path(graph, start, finish)
    print(f'The shortest path (lowest cost path) between vertices {start} and {finish} is {path}'
          f' and its cost is {cost}.')


if __name__ == '__main__':
    main()
