"""
https://www.hackerrank.com/challenges/most-commons/problem
"""
from collections import Counter, defaultdict


def most_common_letters(text):
    frequencies = Counter(text)
    # Sort by descending frequency and alphabetically
    ordered = sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))
    return ordered[:3]


def most_common_letters(text):
    frequencies = Counter(text)
    # Successive sorts in reversed order
    # sort alphabetically
    s = sorted(frequencies.items(), key=lambda x: x[0])
    # sort descending by frequency
    ordered = sorted(s, key=lambda x: x[1], reverse=True)
    return ordered[:3]


def echo(pairs):
    for pair in pairs:
        print(pair[0], pair[1])


def main():
    s = input()
    most_common = most_common_letters(s)
    echo(most_common)


if __name__ == '__main__':
    main()
