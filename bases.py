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
    assert 2 <= base <= len(alphabet)

    if not is_valid(representation, base, alphabet):
        raise ValueError('"{}" is not a valid base {} representation!'.format(representation, base))

    result = 0
    multiplier = 1

    for char in representation[::-1]:
        result += alphabet.index(char) * multiplier
        multiplier *= base
    return result


def to_base(decimal, base, alphabet=ALPHABET):
    assert 2 <= base <= len(alphabet)

    if decimal == 0:
        return '0'

    representation = ''

    while decimal > 0:
        remainder = decimal % base
        representation = alphabet[remainder] + representation
        decimal //= base

    return representation


def print_all_numbers(*, base, digits=2):
    choices = ALPHABET[:base]
    cartesian_product = itertools.product(choices, repeat=digits)
    representations = (''.join(item) for item in cartesian_product)

    for representation in representations:
        print('{}    {}'.format(representation, to_decimal(representation, base)))


def main():

    print('Base 16 to decimal')
    for representation in (x+x for x in ALPHABET[:16]):
        print('{}    {}'.format(representation, to_decimal(representation, 16)))

    print()
    print('Decimal to Base 62')
    for nr in (10**i for i in range(10)):
        print('{:>13,d}     {}'.format(nr, to_base(nr, 62)))


if __name__ == '__main__':
    main()
