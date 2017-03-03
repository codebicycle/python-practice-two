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

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
    xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
    ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

How many strings are nice under these new rules?

"""
import re

BAD = re.compile(r'ab|cd|pq|xy')
THREE_VOWELS = re.compile(r'[aeiou].*[aeiou].*[aeiou]')
DUPLICATE = re.compile(r'(\w)\1')
DUPLICATE_PAIR = re.compile(r'(\w)(\w).*\1\2')
ABA = re.compile(r'(\w)\w\1')


def is_nice(text):
    if BAD.search(text):
        return False
    elif THREE_VOWELS.search(text) and DUPLICATE.search(text):
        return True

    return False


def is_nice2(text):
    if ABA.search(text) and DUPLICATE_PAIR.search(text):
        return True

    return False


def count(lines, callback):
    counter = 0
    for line in lines:
        if callback(line):
            counter += 1

    return counter


def main():
    with open('input5.txt') as f:
        lines = f.readlines()

    num_nice = count(lines, is_nice)
    print(num_nice)

    num_nice = count(lines, is_nice2)
    print(num_nice)


if __name__ == '__main__':
    main()
