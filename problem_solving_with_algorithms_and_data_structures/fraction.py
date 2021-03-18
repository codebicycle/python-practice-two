"""
Problem Solving with Algorithms and Data Structures using Python
https://runestone.academy/runestone/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#a-fraction-class
"""


def gcd(m, n):
    """
    Euclid’s Algorithm states that the greatest common divisor of two integers m and n
    is n if n divides m evenly.
    However, if n does not divide m evenly, then the answer is
    the greatest common divisor of n and the remainder of m divided by n.
    """
    remainder = m % n
    if remainder == 0:
        return n
    return gcd(n, remainder)


def gcd(m, n):
    while m % n != 0:
        old_m = m

        m = n
        n = old_m % n
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.numerator = top
        self.denominator = bottom

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        common = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator//common, new_denominator//common)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        common = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator//common, new_denominator//common)

    def __truediv__(self, other):
        other_reversed = Fraction(other.denominator, other.numerator)
        return self * other_reversed

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        common = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator//common, new_denominator//common)

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator


if __name__ == '__main__':
    f1 = Fraction(1, 4) + Fraction(1, 2)
    print('I ate', f1, 'of the pizza')

    assert gcd(7, 21) == 7
    assert gcd(2, 3) == 1
    assert Fraction(2, 4) == Fraction(1, 2)
    assert Fraction(6, 6) == Fraction(1, 1)
    assert Fraction(1, 4) + Fraction(1, 2) == Fraction(3, 4)
    assert Fraction(2, 3) / Fraction(3, 2) == Fraction(4, 9)
    assert Fraction(3, 4) - Fraction(1, 2) == Fraction(1, 4)
    assert Fraction(3, 4) > Fraction(1, 2)
    assert Fraction(1, 4) < Fraction(1, 2)
