"""Write a function, solve(formula) that solves cryptarithmetic puzzles.
The input should be a formula like 'ODD + ODD == EVEN', and the
output should be a string with the digits filled in, or None if the
problem is not solvable.

"""
import string
import itertools


def output(func):
    def wrapper(formula):
        print(formula)
        result = func(formula)
        print(result)
        print()
        return result

    return wrapper


@output
def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    digits = tuple('0123456789')
    alphabet = set(string.ascii_uppercase)

    unique_letters = set(char
                         for char in formula.upper()
                         if char in alphabet)
    letters = tuple(unique_letters)

    digit_permutations = itertools.permutations(digits, len(letters))
    for permutation in digit_permutations:
        table = str.maketrans(dict(zip(letters, permutation)))
        digit_formula = formula.translate(table)

        try:
            result = eval(digit_formula)
            if result:
                return digit_formula
        except SyntaxError:
            pass


def main():
    solve('ODD + ODD == EVEN')
    solve('A + B == C')
    solve('ABC + ABC == MNOP')
    # solve('ABC + XYZ == MNOP')


if __name__ == '__main__':
    main()
