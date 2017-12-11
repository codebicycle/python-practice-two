ARABIC_NUMERALS = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
ROMAN_NUMERALS = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

def roman(number):
    roman_str = ''
    for i in range(len(ARABIC_NUMERALS)):
        while number >= ARABIC_NUMERALS[i]:
            roman_str += ROMAN_NUMERALS[i]
            number -= ARABIC_NUMERALS[i]

    return roman_str
