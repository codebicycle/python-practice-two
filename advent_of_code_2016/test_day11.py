from advent_of_code_2016.day11 import is_valid


def test_is_valid():
    floor = ('SG', 'PM')
    assert is_valid(floor) is False

    floor = ('SG', 'PM', 'LG')
    assert is_valid(floor) is False

    floor = ('SG', 'SM', 'LG')
    assert is_valid(floor)

    floor = ('SG', 'SM', 'LM')
    assert is_valid(floor) is False

    floor = tuple()
    assert is_valid(floor)

    floor = ('HM', )
    assert is_valid(floor)

    floor = ('HG', )
    assert is_valid(floor)
