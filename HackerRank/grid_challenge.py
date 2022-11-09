def gridChallenge(grid):
    grid = [sorted(row) for row in grid]
    transposed = transpose(grid)
    return 'YES' if is_sorted(transposed) else 'NO'


def transpose(arr):
    transposed = []
    first = arr[0]
    for idx in range(len(first)):
        new_row = ''
        for row in arr:
            new_row += row[idx]
        transposed.append(new_row)
    return transposed


def is_sorted(grid):
    for row in grid:
        if row != ''.join(sorted(row)):
            return False
    return True


if __name__ == '__main__':
    grid = ['abc', 'ade', 'efg']
    expected = "YES"
    result = gridChallenge(grid)
    assert result == expected
