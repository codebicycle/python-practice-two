
MAPPING = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}
DESCENDING_DENOMINATIONS = sorted(MAPPING, reverse=True)

def roman_naive(number):
    if number < 1:
        raise ValueError('Only positive integers greater or equal to 1.')

    if number in MAPPING:
        return MAPPING[number]

    result = ''
    for denomination in DESCENDING_DENOMINATIONS:
        if number >= denomination:
            quotient = number // denomination
            remainder = number % denomination

            result += quotient * MAPPING[denomination]
            if remainder:
                result += roman_naive(remainder)

            return result

def roman_substitution(roman_str):
    SUBSTITUTIONS = {
        'VIIII': 'IX',
        'IIII': 'IV',
        'LXXXX': 'XC',
        'XXXX': 'XL',
        'DCCCC': 'CM',
        'CCCC': 'CD',
    }
    for old, new in SUBSTITUTIONS.items():
        roman_str = roman_str.replace(old, new)

    return roman_str

def roman(number):
    without_substitutions = roman_naive(number)
    roman_str = roman_substitution(without_substitutions)
    return roman_str
