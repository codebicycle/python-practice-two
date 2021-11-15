import pytest

from graph import (find_path, find_all_paths,
                   find_shortest_path)


@pytest.fixture
def graph():
    return {'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C'], }


def test_find_path(graph):
    pass


def test_find_all_paths(graph):
    pass


def test_find_shortest_path(graph):
    pass
