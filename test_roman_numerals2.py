import csv
import os

import pytest

from roman_numerals2 import (to_roman, OutOfRangeError, NotIntegerError,
                             from_roman)

HERE = os.path.dirname(__file__)

@pytest.fixture
def decimal_roman():
    """List of mappings from decimal to roman
    Both decimal and roman are strings
    """
    filepath = os.path.join(HERE, 'roman_numerals.csv')
    with open(filepath, 'r') as f:
        return list(csv.DictReader(f))


def test_to_roman_sample_values():
    assert 'I' == to_roman(1)
    assert 'II' == to_roman(2)
    assert 'III' == to_roman(3)
    assert 'IV' == to_roman(4)
    assert 'V' == to_roman(5)
    assert 'VI' == to_roman(6)
    assert 'VII' == to_roman(7)
    assert 'VIII' == to_roman(8)
    assert 'IX' == to_roman(9)
    assert 'X' == to_roman(10)
    assert 'L' == to_roman(50)
    assert 'C' == to_roman(100)
    assert 'D' == to_roman(500)
    assert 'M' == to_roman(1000)

def test_to_roman_exhaustive(decimal_roman):
    for row in decimal_roman:
        decimal = int(row['decimal'])
        assert row['roman'] == to_roman(decimal)

def test_to_roman_raises_exception_for_out_of_range_integers():
    with pytest.raises(OutOfRangeError):
        to_roman(4000)

    with pytest.raises(OutOfRangeError):
        to_roman(0)

    with pytest.raises(OutOfRangeError):
        to_roman(-1)

def test_to_roman_raises_exception_for_non_integers():
    with pytest.raises(NotIntegerError):
        to_roman(1.0)

    with pytest.raises(NotIntegerError):
        to_roman('string')

    with pytest.raises(NotIntegerError):
        to_roman('0.5')


def test_from_roman_good_values():
    for n in range(1, 4000):
        assert n == from_roman(to_roman(n))
