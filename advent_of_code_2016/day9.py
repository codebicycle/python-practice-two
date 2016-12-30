"""
--- Day 9: Explosives in Cyberspace ---

Wandering around a secure area, you come across a datalink port to a new part of the network. After briefly scanning it for interesting files, you find one file in particular that catches your attention. It's compressed with an experimental format, but fortunately, the documentation for the format is nearby.

The format compresses a sequence of characters. Whitespace is ignored. To indicate that some sequence should be repeated, a marker is added to the file, like (10x2). To decompress this marker, take the subsequent 10 characters and repeat them 2 times. Then, continue reading the file after the repeated data. The marker itself is not included in the decompressed output.

If parentheses or other characters appear within the data referenced by a marker, that's okay - treat it like normal data, not a marker, and then resume looking for markers after the decompressed section.

For example:

    ADVENT contains no markers and decompresses to itself with no changes, resulting in a decompressed length of 6.
    A(1x5)BC repeats only the B a total of 5 times, becoming ABBBBBC for a decompressed length of 7.
    (3x3)XYZ becomes XYZXYZXYZ for a decompressed length of 9.
    A(2x2)BCD(2x2)EFG doubles the BC and EF, becoming ABCBCDEFEFG for a decompressed length of 11.
    (6x1)(1x3)A simply becomes (1x3)A - the (1x3) looks like a marker, but because it's within a data section of another marker, it is not treated any differently from the A that comes after it. It has a decompressed length of 6.
    X(8x2)(3x3)ABCY becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of 18), because the decompressed data from the (8x2) marker (the (3x3)ABC) is skipped and not processed further.

What is the decompressed length of the file (your puzzle input)? Don't count whitespace.

--- Part Two ---

Apparently, the file actually uses version two of the format.

In version two, the only difference is that markers within decompressed data are decompressed. This, the documentation explains, provides much more substantial compression capabilities, allowing many-gigabyte files to be stored in only a few kilobytes.

For example:

    (3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no markers.
    X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data from the (8x2) marker is then further decompressed, thus triggering the (3x3) marker twice for a total of six ABC sequences.
    (27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated 241920 times.
    (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 characters long.

Unfortunately, the computer you brought probably doesn't have enough memory to actually decompress the file; you'll have to come up with another way to get its decompressed length.

What is the decompressed length of the file using this improved format?

"""
import copy
import re

MARKER = re.compile(r'\((\d+)x(\d+)\)')


def parse_recursive(content, message):
    match = MARKER.search(content)
    if match:
        length = int(match.group(1))
        multiplier = int(match.group(2))
        start = match.start()
        end = match.end()

        message.append(content[:start])
        message.append(content[end:end + length] * multiplier)
        content = content[end + length:]
        parse_recursive(content, message)
    else:
        message.append(content)


def decode(content):
    # content = re.sub(r'\s', '', content)

    accumulator = []
    parse_recursive(content, accumulator)
    message = ''.join(accumulator)
    return message


def decode_deep(content):
    representation = build_representation(content)

    clone = copy.deepcopy(representation)
    while any(isinstance(i, list) for i in clone):
        clone = expand_representation(clone)

    message = ''.join(clone)
    return message, len(message)


def build_representation(content):
    if not content:
        return []

    representation = []
    match = MARKER.search(content)
    if match:
        length = int(match.group(1))
        multiplier = int(match.group(2))
        start = match.start()
        end = match.end()

        if start != 0:
            representation.append(build_representation(content[:start]))

        if multiplier:
            inside = [multiplier,
                      build_representation(content[end: end + length])]
            representation.append(inside)

        if end + length != match.endpos:
            representation.extend(build_representation(content[end + length:]))
    else:
        representation.append(content)

    return representation


def expand_representation(array):
    hold = []
    for item in array:

        if isinstance(item, list):
            if len(item) == 1:
                hold.append(item[0])
            elif any(isinstance(i, list) for i in item):
                hold.append(expand_representation(item))
            elif isinstance(item[0], int):
                multiplier = item[0]
                hold.extend([multiplier * i for i in item[1:]])
            else:
                hold.extend(item[:])
        else:
            hold.append(item)

    return hold


def calculate_message_length(content):
    size = 0
    match = MARKER.search(content)
    if match:
        length = int(match.group(1))
        multiplier = int(match.group(2))
        start = match.start()
        end = match.end()

        size += len(content[:start])
        size += multiplier * calculate_message_length(content[end: end+length])
        size += calculate_message_length(content[end+length:])
    else:
        size += len(content)
    return size


def main():
    with open('input9.txt', 'r') as f:
        content = f.read().strip()

    message = decode(content)
    length = len(message)
    print(length)

    # # WARNING: Unresponsive code! Too slow for the input size
    # message, length = decode_deep(content)
    # print(message[:255])
    # print(length)

    length = calculate_message_length(content)
    print(length)

if __name__ == '__main__':
    main()
