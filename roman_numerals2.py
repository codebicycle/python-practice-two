class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass

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
    result = 0
    index = 0
    while index < len(roman_numeral):
        for roman, integer in roman_numeral_map:
            if roman_numeral[index:index+len(roman)] == roman:
                result += integer
                index += len(roman)
    return result
