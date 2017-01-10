from advent_of_code_2016.day15 import parse, get_start_time


def test_get_start_time():
    input_str = """Disc #1 has 5 positions; at time=0, it is at position 4.
                    Disc #2 has 2 positions; at time=0, it is at position 1."""
    lines = input_str.split('\n')
    disks = parse(lines)
    start_time = get_start_time(disks)
    assert 5 == start_time
