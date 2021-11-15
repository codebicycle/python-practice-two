"""
https://www.hackerrank.com/challenges/merge-the-tools/problem
"""


def merge_the_tools(string, k):
    sequences = merge_the_tools_helper(string, k)
    echo(sequences)


def merge_the_tools_helper(string, k):
    # chunk the string
    chunks = [string[i:i + k] for i in range(0, len(string), k)]
    # process the chunks
    sequences = [unique_keep_order(chunk) for chunk in chunks]
    return sequences


def unique_keep_order(word):
    unique = []
    seen = set()
    for letter in word:
        if letter not in seen:
            unique.append(letter)
            seen.add(letter)
    return ''.join(unique)


def echo(rows):
    for row in rows:
        print(row)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
