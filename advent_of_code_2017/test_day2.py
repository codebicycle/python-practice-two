from day2 import checksum, checksum_divisible

def test_examples():
    puzzle_input = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
    assert 18 == checksum(puzzle_input)

def test_examples_part2():
    puzzle_input = [[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]
    assert 9 == checksum_divisible(puzzle_input)
