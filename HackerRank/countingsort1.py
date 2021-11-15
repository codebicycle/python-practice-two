"""
https://www.hackerrank.com/challenges/one-month-preparation-kit-countingsort1
"""

RANGE = 100


def countingSort(arr):
    frequencies = [0] * RANGE
    for number in arr:
        frequencies[number] += 1
    return frequencies


if __name__ == '__main__':
    arr = [1, 1, 3, 2, 1]
    expected = [0, 3, 1, 1]
    result = countingSort(arr)
    assert result[:4] == expected
