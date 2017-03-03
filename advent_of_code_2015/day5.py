"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

"""
import re

BAD = re.compile(r'ab|cd|pq|xy')
THREE_VOWELS = re.compile(r'[aeiou].*[aeiou].*[aeiou]')
DUPLICATE = re.compile(r'(\w)\1')


def is_nice(text):
    if BAD.search(text):
        return False
    elif THREE_VOWELS.search(text) and DUPLICATE.search(text):
        return True

    return False


def count_nice(lines):
    counter = 0
    for line in lines:
        if is_nice(line):
            counter += 1

    return counter


def main():
    with open('input5.txt') as f:
        lines = f.readlines()

    num_nice = count_nice(lines)
    print(num_nice)

if __name__ == '__main__':
    main()
