import pytest

from apsp import shortest_path

@pytest.fixture
def graph():
    return {
        0: {1: 2, 4: 4},
        1: {2: 3},
        2: {3: 5, 4: 1 },
        3: {0: 8},
        4: {3: 3},
    }

def test_shortest_path_direct_arc(graph):
    cost, path = shortest_path(graph, 0, 1)
    assert cost == 2
    assert path == [0, 1]

def test_shortest_path_indirect(graph):
    cost, path = shortest_path(graph, 0, 2)
    assert cost == 5
    assert path == [0, 1, 2]

def test_shortest_path_indirect_vs_direct_arc(graph):
    cost, path = shortest_path(graph, 2, 3)
    assert cost == 4
    assert path == [2, 4, 3]

def test_shortest_path_longer_path(graph):
    cost, path = shortest_path(graph, 2, 0)
    assert cost == 12
    assert path == [2, 4, 3, 0]
