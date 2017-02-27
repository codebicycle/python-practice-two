
from pairs_sum import pairs_that_sum

def test_one_pair():
    numbers = [5, 1, 2, 20, 15]
    total = 20
    expected = [(5, 15),]
    result = pairs_that_sum(numbers, total)
    assert expected == sorted(result)


def test_multiple_pairs():
    numbers = [9, 1, 2, 8, 15]
    total = 10
    expected = [(1, 9), (2, 8)]
    result = pairs_that_sum(numbers, total)
    assert expected == sorted(result)


def test_negative_number():
    numbers = [-7, -5, 1, 10, 15]
    total = 10
    expected = [(-5, 15),]
    result = pairs_that_sum(numbers, total)
    assert expected == sorted(result)


def test_duplicates_right():
    numbers = [-48, 96, 96, 96]
    total = 48
    expected = [(-48, 96),]
    result = pairs_that_sum(numbers, total)
    assert expected == sorted(result)


def test_duplicates_left():
    numbers = [-48, -48, -48, 96]
    total = 48
    expected = [(-48, 96),]
    result = pairs_that_sum(numbers, total)
    assert expected == sorted(result)


def test_duplicates_center():
    numbers = [5, 10, 10, 20]
    total = 20
    expected = [(10, 10),]
    result = pairs_that_sum(numbers, total)
    assert expected == sorted(result)


def test_all_duplicate():
    numbers = [5, 5, 5, 5]
    total = 10
    expected = [(5, 5),]
    result = pairs_that_sum(numbers, total)
    assert expected == sorted(result)


def test_no_pairs():
    numbers = [2, 3, 4, 5]
    total = 10
    expected = []
    result = pairs_that_sum(numbers, total)
    assert expected == sorted(result)
