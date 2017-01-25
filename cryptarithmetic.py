"""Write a function, solve(formula) that solves cryptarithmetic puzzles.
The input should be a formula like 'ODD + ODD == EVEN', and the
output should be a string with the digits filled in, or None if the
problem is not solvable.

"""
import re
import string
import itertools

import time

FIRST_LETTER = re.compile(r'\b[a-zA-Z]')
LETTER = re.compile(r'[a-zA-Z]')


def output(func):
    def wrapper(formula):
        print(formula)
        start_time = time.perf_counter()
        substitution = func(formula)
        elapsed_time = time.perf_counter() - start_time
        print(substitution)
        print('{:.3f} seconds'.format(elapsed_time))
        print()
        return substitution

    return wrapper


@output
def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    formula = formula.upper()

    digits = tuple('0123456789')
    alphabet = set(string.ascii_uppercase)

    unique_first_letters = set(FIRST_LETTER.findall(formula))
    unique_letters = set(LETTER.findall(formula))
    rest = unique_letters - unique_first_letters
    letters = tuple(unique_first_letters) + tuple(rest)
    end_first_letters = len(unique_first_letters)

    digit_permutations = itertools.permutations(digits, len(letters))
    for permutation in digit_permutations:
        if '0' in permutation[:end_first_letters]:
            continue

        table = str.maketrans(dict(zip(letters, permutation)))
        digit_formula = formula.translate(table)

        result = eval(digit_formula)
        if result:
            return digit_formula


def main():
    solve('ODD + ODD == EVEN')
    solve('A + B == C')
    solve('ABC + ABC == MNOP')
    solve('ABC + XYZ == MNOP')


if __name__ == '__main__':
    main()
