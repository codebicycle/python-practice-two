"""
https://www.hackerrank.com/challenges/one-month-preparation-kit-diagonal-difference/problem
"""


def diagonalDifference(arr):
    n = len(arr)
    left_to_right_diagonal = [arr[i][i] for i in range(n)]
    right_to_left_diagonal = [arr[i][n - 1 - i] for i in range(n)]
    # right_to_left_diagonal = [arr[i][j] for i, j in zip(range(n), range(n - 1, -1, -1))]
    return abs(sum(left_to_right_diagonal) - sum(right_to_left_diagonal))


if __name__ == '__main__':
    arr = [[1, 2, 3],
           [4, 5, 6],
           [9, 8, 9]]
    expected = 2
    result = diagonalDifference(arr)
    assert result == expected
