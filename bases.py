"""Base 2 to base 62, convert to and from decimal"""

import string
import itertools
import collections

REMOVE_AMBIGUOUS = str.maketrans('', '', '0OIl')

ALPHABET = string.digits + string.ascii_uppercase + string.ascii_lowercase
ALPHABET_UNAMBIGUOUS = ALPHABET.translate(REMOVE_AMBIGUOUS)

DIGIT_LOWER_UPPER = string.digits + string.ascii_lowercase + string.ascii_uppercase
DIGIT_LOWER_UPPER_UNAMBIGUOUS = DIGIT_LOWER_UPPER.translate(REMOVE_AMBIGUOUS)


def is_valid(representation, base, alphabet=ALPHABET):
    """Check if representation is valid for given base
    @representation str
    @base int
    @alphabet str

    """
    assert 2 <= base <= len(alphabet)
    return not any(char
                   for char in representation
                   if char not in alphabet[:base])


def to_decimal(representation, base, alphabet=ALPHABET):
    """Convert the string representation of a number in a given base
    to decimal.

    representation: string representation of a number in a given base
    base: the base of the input representation
    alphabet: sequence of characters representing digits (and letters)
    in their corresponding possition e.g. for base 16 '0123456789abcdef'
    Returns an integer in base 10
    """
    assert 2 <= base <= len(alphabet)

    if not is_valid(representation, base, alphabet):
        raise ValueError(f'"{representation}" is not a valid base {base} representation!')

    decimal = 0
    multiplier = 1

    for char in reversed(representation):
        decimal += alphabet.index(char) * multiplier
        multiplier *= base
    return decimal


def to_base(decimal, base, alphabet=ALPHABET):
    """Convert from decimal to the given base

    decimal: positive base 10 integer to be converted
    base: the base to be converted to
    alphabet: sequence of characters representing digits (and letters)
    in their corresponding possition e.g. for base 16 '0123456789abcdef'
    Returns the string representation of the decimal in the given base.
    """
    assert 2 <= base <= len(alphabet)
    assert decimal >= 0

    if decimal == 0:
        return '0'

    stack = []
    while decimal > 0:
        remainder = decimal % base
        stack.append(alphabet[remainder])
        decimal =  decimal // base

    # representation = ''.join([stack.pop() for _ in stack])
    representation = ''.join(reversed(stack))
    return representation


def print_all_numbers(*, base, digits=2):
    choices = ALPHABET[:base]
    cartesian_product = itertools.product(choices, repeat=digits)
    representations = (''.join(item) for item in cartesian_product)

    for representation in representations:
        print(f'{representation}    {to_decimal(representation, base)}')


def main():

    print('Base 16 to decimal')
    for representation in (x+x for x in ALPHABET[:16]):
        print(f'{representation}    {to_decimal(representation, 16)}')

    print()
    print('Decimal to Base 62')
    for num in (10**i for i in range(10)):
        print(f'{num:>13,d}     {to_base(num, 62)}')


if __name__ == '__main__':
    main()
