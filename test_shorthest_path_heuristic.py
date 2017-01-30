import pytest

from shorthest_path_heuristic import outside, parse, Cell, is_open

@pytest.fixture
def maze():
    maze_str = """
           ..#
           ##.
           ..#
       """
    maze_array = parse(maze_str)
    return maze_array


def test_outside():
    assert outside(3, 3)
    assert outside(0, 3) is False
    assert outside(2, 3) is False
    assert outside(-1, 3)
    assert outside(4, 3)


def test_parse():
    maze_str = """
        ..#
        ..#
        ###
    """
    maze = parse(maze_str)
    expected = (('.', '.', '#'),
                ('.', '.', '#'),
                ('#', '#', '#'))
    assert expected == maze


def test_is_open(maze):
    cell = Cell(0, 0)
    assert is_open(cell, maze)

    cell = Cell(2, 0)
    assert is_open(cell, maze) is False

    cell = Cell(0, 1)
    assert is_open(cell, maze) is False

    cell = Cell(1, 1)
    assert is_open(cell, maze) is False

    cell = Cell(2, 2)
    assert is_open(cell, maze) is False

    cell = Cell(1, 2)
    assert is_open(cell, maze)


