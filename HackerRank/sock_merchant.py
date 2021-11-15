import collections


def sockMerchant(n, arr):
    counter = collections.Counter(arr)
    pairs = 0
    for count in counter.values():
        pairs += count // 2
    return pairs


if __name__ == '__main__':
    arr = [1, 2, 1, 2, 1, 3, 2]
    expected = 2
    result = sockMerchant(len(arr), arr)
    assert result == expected
