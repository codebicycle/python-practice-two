from advent_of_code_2016.day1 import get_distance


def test_get_distance():
    assert 5 == get_distance('R2, R3')
    assert 2 == get_distance('R2, R2, R2')
    assert 12 == get_distance('R5, L5, R5, R3')
