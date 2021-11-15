"""
https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem
"""


def plus_minus(arr, n):
    positives, negatives, zeros = 0, 0, 0
    for number in arr:
        if number > 0:
            positives += 1
        elif number < 0:
            negatives += 1
        else:
            zeros += 1

    positives_ratio = positives / n
    negative_ratio = negatives / n
    zero_ratio = zeros / n

    print(f'{positives_ratio:.6f}')
    print(f'{negative_ratio:.6f}')
    print(f'{zero_ratio:.6f}')


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr, n)
