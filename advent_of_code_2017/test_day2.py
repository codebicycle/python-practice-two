from day2 import checksum, read_input

def test_examples():
    puzzle_input = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
    assert 18 == checksum(puzzle_input)
