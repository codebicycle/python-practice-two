"""
--- Day 21: Scrambled Letters and Hash ---

The computer system you're breaking into uses a weird scrambling function to store its passwords. It shouldn't be much trouble to create your own scrambled password so you can add it to the system; you just have to implement the scrambler.

The scrambling function is a series of operations (the exact list is provided in your puzzle input). Starting with the password to be scrambled, apply each operation in succession to the string. The individual operations behave as follows:

    swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
    swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string).
    rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
    rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
    reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
    move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.

For example, suppose you start with abcde and perform the following operations:

    swap position 4 with position 0 swaps the first and last letters, producing the input for the next step, ebcda.
    swap letter d with letter b swaps the positions of d and b: edcba.
    reverse positions 0 through 4 causes the entire string to be reversed, producing abcde.
    rotate left 1 step shifts all letters left one position, causing the first letter to wrap to the end of the string: bcdea.
    move position 1 to position 4 removes the letter at position 1 (c), then inserts it at position 4 (the end of the string): bdeac.
    move position 3 to position 0 removes the letter at position 3 (a), then inserts it at position 0 (the front of the string): abdec.
    rotate based on position of letter b finds the index of letter b (1), then rotates the string right once plus a number of times equal to that index (2): ecabd.
    rotate based on position of letter d finds the index of letter d (4), then rotates the string right once, plus a number of times equal to that index, plus an additional time because the index was at least 4, for a total of 6 right rotations: decab.

After these steps, the resulting scrambled password is decab.

Now, you just need to generate a new scrambled password and you can access the system. Given the list of scrambling operations in your puzzle input, what is the result of scrambling abcdefgh?

--- Part Two ---

You scrambled the password correctly, but you discover that you can't actually modify the password file on the system. You'll need to un-scramble one of the existing passwords by reversing the scrambling process.

What is the un-scrambled version of the scrambled password fbgdceah?

"""
import re

ROTATE_RIGHT = re.compile(r'rotate right (\d+)')
ROTATE_LEFT = re.compile(r'rotate left (\d+)')
ROTATE_LETTER = re.compile(r'rotate based on position of letter (\w)')
SWAP_POSITION = re.compile(r'swap position (\d+) with position (\d+)')
SWAP_LETTER = re.compile(r'swap letter (\w) with letter (\w)')
REVERSE = re.compile(r'reverse positions (\d+) through (\d+)')
MOVE = re.compile(r'move position (\d+) to position (\d+)')


def rotate(chars, steps):
    index = steps % len(chars)
    rotated = chars[index:] + chars[:index]
    return rotated


def rotate_right(chars, *args):
    steps = -int(args[0])
    return rotate(chars, steps)


def rotate_left(chars, *args):
    steps = int(args[0])
    return rotate(chars, steps)


def rotate_based_on_letter_position(chars, *args):
    letter = args[0]
    index = chars.index(letter)
    if index >= 4:
        rotated = rotate_right(chars, index + 2)
    else:
        rotated = rotate_right(chars, index + 1)
    return rotated


def undo_rotate_based_on_letter_position(chars, *args):
    # {index: rotation_steps}
    rot = {index: index + 1 if index < 4 else index + 2
           for index in range(len(chars))}
    length = len(chars)

    # {index_after_rotation: rotation_steps}
    rot_opposite = {(index + rot[index]) % length: rot[index]
                    for index in rot}
    letter = args[0]
    index = chars.index(letter)

    return rotate_left(chars, rot_opposite[index])


def swap_position(chars, *args):
    clone = chars.copy()
    idx1 = int(args[0])
    idx2 = int(args[1])
    clone[idx1], clone[idx2] = clone[idx2], clone[idx1]
    return clone


def undo_swap_position(chars, *args):
    return swap_position(chars, args[1], args[0])


def swap_letter(chars, *args):
    letter1, letter2 = args
    swapped = [letter1 if char == letter2 else
               letter2 if char == letter1 else char
               for char in chars]
    return swapped


def reverse_from(chars, *args):
    clone = chars.copy()
    idx1 = int(args[0])
    idx2 = int(args[1])
    segment = clone[idx1: idx2 + 1]
    reversed_segment = reversed(segment)
    clone[idx1: idx2 + 1] = reversed_segment
    return clone


def move(chars, *args):
    clone = chars.copy()
    idx1 = int(args[0])
    idx2 = int(args[1])
    letter = clone.pop(idx1)
    clone.insert(idx2, letter)
    return clone


def undo_move(chars, *args):
    return move(chars, args[1], args[0])


def apply_matching_transformation(input_str, line, commands, undo=False):
    matched = False
    for item in commands:
        match = item['regex'].match(line)
        if match:
            matched = True
            if undo is True:
                result = item['undo_callback'](input_str, *match.groups())
            else:
                result = item['callback'](input_str, *match.groups())
            break
    if not matched:
        raise ValueError("Unable to parse command on line: '{}'"
                         .format(line.strip()))

    return result


def scramble(password, lines, commands):
    code = tuple(password)
    for line in lines:
        code = apply_matching_transformation(code, line, commands)
    return ''.join(code)


def unscramble(code, lines, commands):
    password = list(code)
    for line in reversed(lines):
        password = apply_matching_transformation(password, line, commands,
                                                 undo=True)
    return ''.join(password)


def main():
    with open('input21.txt', 'r') as f:
        lines = f.readlines()

    commands = [
        {
            'regex': ROTATE_RIGHT,
            'callback': rotate_right,
            'undo_callback': rotate_left,
        },
        {
            'regex': ROTATE_LEFT,
            'callback': rotate_left,
            'undo_callback': rotate_right,
        },
        {
            'regex': ROTATE_LETTER,
            'callback': rotate_based_on_letter_position,
            'undo_callback': undo_rotate_based_on_letter_position,
        },
        {
            'regex': SWAP_POSITION,
            'callback': swap_position,
            'undo_callback': undo_swap_position,
        },
        {
            'regex': SWAP_LETTER,
            'callback': swap_letter,
            'undo_callback': swap_letter,
        },
        {
            'regex': REVERSE,
            'callback': reverse_from,
            'undo_callback': reverse_from,
        },
        {
            'regex': MOVE,
            'callback': move,
            'undo_callback': undo_move,
        },
    ]

    password = 'abcdefgh'
    scrambled = scramble(password, lines, commands)
    print('Scramble {} => {}'.format(password, scrambled))

    # Part 2
    scrambled = 'fbgdceah'
    unscrambled = unscramble(scrambled, lines, commands)
    print('Unscramble {} => {}'.format(scrambled, unscrambled))


if __name__ == '__main__':
    main()
