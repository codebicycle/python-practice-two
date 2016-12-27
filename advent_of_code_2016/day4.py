"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

    aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
    a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
    not-a-real-room-404[oarel] is a real room.
    totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

"""

import re

import collections

LETTERS_RE = re.compile(r'([-a-z]*)-')
DIGITS_RE = re.compile(r'\b(\d+)\b')
CHECKSUM_RE = re.compile(r'\[([a-z]+)\]')


def parse(line):
    sectorid = None
    name = None
    checksum = None

    match = DIGITS_RE.search(line)
    if match:
        sectorid = int(match.group(1))

    match = LETTERS_RE.search(line)
    if match:
        name = match.group(1)

    match = CHECKSUM_RE.search(line)
    if match:
        checksum = match.group(1)

    return name, sectorid, checksum


def is_valid(name, checksum):
    name = re.sub('-', '', name)
    frequencies = collections.Counter(name)
    ordered = sorted(frequencies, key=lambda x: (-frequencies[x], x))
    computed_checksum = ''.join(ordered[:5])
    return checksum == computed_checksum


def main():
    with open('input4.txt', 'r') as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        name, sectorid, checksum = parse(line)
        if is_valid(name, checksum):
            total += sectorid

    print(total)


if __name__ == '__main__':
    main()
