"""
https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/problem
"""
import collections


def matching_strings(strings, queries):
    # Re-iterate strings for each query
    results = [strings.count(query) for query in queries]
    return results


def matching_strings(strings, queries):
    # Iterate through strings once
    counter = collections.Counter(strings)
    results = [counter[query] for query in queries]
    return results


if __name__ == '__main__':
    strings = ['ab', 'ab', 'abc']
    queries = ['ab', 'abc', 'bc']

    results = matching_strings(strings, queries)
    expected = [2, 1, 0]
    assert results == expected
