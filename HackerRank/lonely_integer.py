"""
https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem
"""
import collections


def lonely_integer(numbers):
    counter = collections.Counter(numbers)
    # key of the last most_common item
    return counter.most_common()[-1][0]


def lonely_integer(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            seen.remove(number)
        else:
            seen.add(number)

    assert len(seen) == 1
    return seen.pop()


if __name__ == '__main__':
    a = [1, 2, 3, 4, 3, 2, 1]
    expected = 4
    assert lonely_integer(a) == expected
