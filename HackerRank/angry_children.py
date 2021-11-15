def maxMin(k, arr):
    """Calculate the rolling(k) unfairness for the array
    Keep the minimum value
    """
    ordered = sorted(arr)
    min_unfairness = float('inf')
    # for candidates in set(rolling_iterator(k, ordered)):
    for candidates in rolling_iterator(k, ordered):
        current_unfairness = unfairness(candidates)
        if current_unfairness < min_unfairness:
            min_unfairness = current_unfairness

    return min_unfairness


# def maxMin(k, arr):
#     """Calculate the rolling(k) unfairness for the array
#     Keep the minimum value
#     """
#     ordered = sorted(arr)
#     return min(map(unfairness, rolling_iterator(k, ordered)))


def rolling_iterator(k, arr):
    """iterate an array k elements at a time"""
    i = 0
    while i + k <= len(arr):
        yield arr[i:i + k]
        i += 1


def rolling_iterator(k, arr):
    """iterate an array k elements at a time"""
    i = 0
    while i + k <= len(arr):
        yield tuple(sorted(arr[i:i + k]))
        i += 1


def unfairness(arr):
    return max(arr) - min(arr)


def maxMin(k, arr):
    """Iterate over the sorted list, without creating intermediate lists"""
    ordered = sorted(arr)
    min_unfairness = float('inf')
    for i in range(len(arr) - k + 1):
        current_unfairness = ordered[i + k -1] - ordered[i]
        if current_unfairness < min_unfairness:
            min_unfairness = current_unfairness
    return min_unfairness


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
    k = 4
    expected = 3
    assert maxMin(k, arr) == expected

    arr = [1, 10, 10, 10, 10]
    k = 4
    expected = 0
    assert maxMin(k, arr) == expected
