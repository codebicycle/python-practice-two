from advent_of_code_2016.day20 import group_intervals


def test_group_intervals():
    raw_intervals = [(5, 8), (0, 2), (4, 7)]
    intervals = group_intervals(raw_intervals)
    expected = [(0, 2), (4, 8)]
    assert expected == intervals
