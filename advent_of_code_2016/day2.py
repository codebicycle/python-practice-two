"""
--- Day 2: Bathroom Security ---

You arrive at Easter Bunny Headquarters under cover of darkness. However, you left in such a rush that you forgot to use the bathroom! Fancy office buildings like this one usually have keypad locks on their bathrooms, so you search the front desk for the code.

"In order to improve security," the document you find says, "bathroom codes will no longer be written down. Instead, please memorize and follow the procedure below to access the bathrooms."

The document goes on to explain that each button to be pressed can be found by starting on the previous button and moving to adjacent buttons on the keypad: U moves up, D moves down, L moves left, and R moves right. Each line of instructions corresponds to one button, starting at the previous button (or, for the first line, the "5" button); press whatever button you're on at the end of each line. If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom. You picture a keypad like this:

1 2 3
4 5 6
7 8 9

Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD

    You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.
    Starting from the previous button ("1"), you move right twice (to "3") and then down three times (stopping at "9" after two moves and ignoring the third), ending up with 9.
    Continuing from "9", you move left, up, right, down, and left, ending with 8.
    Finally, you move up four times (stopping at "2"), then down once, ending with 5.

So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front desk. What is the bathroom code?


--- Part Two ---

You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D

You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:

    You start at "5" and don't move at all (up and left are both edges), ending at 5.
    Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
    Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
    Finally, after five more moves, you end at 3.

So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom code?

"""

# origin top-left, (y, x)
DIRECTIONS = {
    'u': (-1, 0),   # up
    'r': (0, 1),    # right
    'd': (1, 0),    # down
    'l': (0, -1),   # left
}

KEYPAD_CLASSIC = {
    (0, 0): 1, (0, 1): 2, (0, 2): 3,
    (1, 0): 4, (1, 1): 5, (1, 2): 6,
    (2, 0): 7, (2, 1): 8, (2, 2): 9,
    'start': (1, 1),
}

KEYPAD_DIAMOND = {
                          (0, 2): 1,
               (1, 1): 2, (1, 2): 3, (1, 3): 4,
    (2, 0): 5, (2, 1): 6, (2, 2): 7, (2, 3): 8, (2, 4): 9,
             (3, 1): 'A', (3, 2): 'B', (3, 3): 'C',
                          (4, 2): 'D',
    'start': (2, 0),
}


def add_tuples(tuple_one, tuple_two):
    return tuple(x + y for x, y in zip(tuple_one, tuple_two))


def get_code(indications, keypad):
    start = keypad['start']
    code = []
    for row in indications.split():
        char, start = get_char(start, row, keypad)
        code.append(char)

    return ''.join(str(item) for item in code)


def get_char(start, row, keypad):
    for direction in row.lower():
        start = move(start, DIRECTIONS[direction], keypad)
    x, y = coordinates = start
    return keypad[x, y], coordinates


def move(start, direction, keypad):
    new_location = add_tuples(start, direction)
    if new_location not in keypad:
        new_location = start
    return new_location


def main():
    with open('input2.txt', 'r') as f:
        indications = f.read()

    code = get_code(indications, KEYPAD_CLASSIC)
    print(code)

    code = get_code(indications, KEYPAD_DIAMOND)
    print(code)


if __name__ == '__main__':
    main()
