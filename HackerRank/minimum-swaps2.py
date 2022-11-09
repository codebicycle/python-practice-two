
# 0  1  2  3  4  5  6
# 7  1  3  2  4  5  6
# 6 -1  0 -2 -1 -1 -1

# 2  1  3  7  4  5  6
# 1 -1  0  3 -1 -1 -1

# 2  1  3  4  7  5  6
# 1 -1  0  0  2 -1 -1


def minimumSwaps(arr):
    deltas = [number - 1 - idx for idx, number in enumerate(arr)]
    swaps = 0
    while True:
        max_delta = max(deltas)
        max_delta_idx = deltas.index(max_delta)
        min_delta = min(deltas[max_delta_idx:])
        min_delta_idx = deltas.index(min_delta)

        if min_delta > 0:
            break
        swaps += 1
        # update deltas
        []






if __name__ == '__main__':
    arr = [7, 1, 3, 2, 4, 5, 6]
    result = minimumSwaps(arr)
    expected = 5
    assert expected == result
