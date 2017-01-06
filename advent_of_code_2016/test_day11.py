from advent_of_code_2016.day11 import is_valid


def test_is_valid():
    state = ('SG', 'PM')
    assert is_valid(state) is False

    state = ('SG', 'PM', 'LG')
    assert is_valid(state) is False

    state = ('SG', 'SM', 'LG')
    assert is_valid(state)

    state = ('SG', 'SM', 'LM')
    assert is_valid(state) is False

    state = tuple()
    assert is_valid(state)

    state = ('HM', )
    assert is_valid(state)

    state = ('HG', )
    assert is_valid(state)
