from functools import reduce


# def maximize_it(arr, M):
#     """Single case, arr of length 3"""
#     results = []
#     first, second, third = arr
#     for x in first:
#         for y in second:
#             for z in third:
#                 current = (x ** 2 + y ** 2 + z ** 2) % M
#                 results.append(current)
#     return max(results)


def maximize_it(arr, m):
    pass
    combinations = get_combinations(arr)
    results = [compute(combination, m) for combination in combinations]
    return max(results)


def compute(collection, m):
    return sum(x ** 2 for x in collection) % m


def get_combinations(arr):
    # TODO: reimplement reduce from scratch
    return reduce(combine, arr)


def combine(list_a, list_b):
    for x in list_a:
        for y in list_b:
            if isinstance(x, tuple):
                yield x + (y,)
            else:
                yield x, y


def read_input():
    arr = []
    k, m = (int(x) for x in input().strip().split())
    for _ in range(k):
        row = tuple(int(x) for x in input().strip().split())
        arr.append(row[1:])
    return tuple(arr), m


if __name__ == '__main__':
    m = 1000
    arr = [(5, 4), (7, 8, 9), (5, 7, 8, 9, 10)]
    expected = 206
    result = maximize_it(arr, m)
    print(result)
    assert result == expected
