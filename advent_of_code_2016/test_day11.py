from advent_of_code_2016.day11 import is_valid


def test_is_valid():
    state = (('SG', 'PM'), 0)
    assert is_valid(state) is False

    state = (('SG', 'PM', 'LG'), 0)
    assert is_valid(state) is False

    state = (('SG', 'SM', 'LG'), 0)
    assert is_valid(state)

    state = (('SG', 'SM', 'LM'), 0)
    assert is_valid(state) is False
