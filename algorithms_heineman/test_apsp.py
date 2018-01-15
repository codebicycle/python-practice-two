import pytest

from apsp import lowest_cost

@pytest.fixture
def graph():
    return {
        0: {1: 2, 4: 4},
        1: {2: 3},
        2: {3: 5, 4: 1 },
        3: {0: 8},
        4: {3: 3},
    }

def test_lowest_cost_direct_arc(graph):
    assert lowest_cost(graph, 0, 1) == 2

def test_lowest_cost_indirect(graph):
    assert lowest_cost(graph, 0, 2) == 5

def test_lowest_cost_indirect_vs_direct_arc(graph):
    assert lowest_cost(graph, 2, 3) == 4
