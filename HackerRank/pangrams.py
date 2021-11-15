"""
https://www.hackerrank.com/challenges/one-month-preparation-kit-pangrams
"""
import string


def is_pangram(text):
    unique = set(text.lower())
    unique.discard(' ')
    alphabet = set(string.ascii_lowercase)
    return unique == alphabet


def pangrams(s):
    return 'pangram' if is_pangram(s) else 'not pangram'


if __name__ == '__main__':
    text = 'The quick brown fox jumps over the lazy dog'
    assert is_pangram(text)

    text = 'We promptly judged antique ivory buckles for the next prize'
    assert is_pangram(text)

    text = 'We promptly judged antique ivory buckles for the prize'
    assert not is_pangram(text)
