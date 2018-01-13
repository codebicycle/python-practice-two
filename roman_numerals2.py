import re


class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass
class InvalidRomanNumeralError(ValueError): pass

ROMAN_NUMERAL_PATTERN = re.compile('''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    ''', re.VERBOSE)

roman_numeral_map = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1),
)

def to_roman(n):
    """Convert arab numeral to roman.

    n must be an integer in the range 1-3999.
    Returns the roman numeral notation as a string.
    """
    if not isinstance(n, int):
        raise NotIntegerError('Expected and integer.')
    if not (0 < n <= 3999):
        raise OutOfRangeError('Expected an integer in the range 1-3999.')

    result = ''
    for roman, integer in roman_numeral_map:
        while n >= integer:
            result += roman
            n -= integer
    return result


def from_roman(roman_numeral):
    """Convert roman to arab numeral."""
    if not ROMAN_NUMERAL_PATTERN.search(roman_numeral):
        raise InvalidRomanNumeralError('Invalid roman numeral.')

    result = 0
    index = 0
    while index < len(roman_numeral):
        for roman, integer in roman_numeral_map:
            if roman_numeral[index:index+len(roman)] == roman:
                result += integer
                index += len(roman)
    return result
