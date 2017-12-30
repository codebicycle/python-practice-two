import pytest

from day22 import Virus, build_grid


@pytest.fixture
def virus():
    grid = build_grid(['.'])
    return Virus(grid)


def test_at_first_virus_is_pointing_north(virus):
    assert virus.NORTH == virus.direction


def test_virus_turn_left(virus):
    virus._turn_left()
    assert virus.WEST == virus.direction

    virus._turn_left()
    assert virus.SOUTH == virus.direction

    virus._turn_left()
    assert virus.EAST == virus.direction

    virus._turn_left()
    assert virus.NORTH == virus.direction


def test_virus_turn_right(virus):
    virus._turn_right()
    assert virus.EAST == virus.direction

    virus._turn_right()
    assert virus.SOUTH == virus.direction

    virus._turn_right()
    assert virus.WEST == virus.direction

    virus._turn_right()
    assert virus.NORTH == virus.direction
