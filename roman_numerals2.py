class OutOfRangeError(ValueError): pass

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
    if not (0 < n <= 3999):
        raise OutOfRangeError('Expected an integer in the range 1-3999.')

    roman_representation = ''
    for roman, integer in roman_numeral_map:
        while n >= integer:
            roman_representation += roman
            n -= integer
    return roman_representation
