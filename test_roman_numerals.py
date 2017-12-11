import csv

import pytest

from roman_numerals import roman

@pytest.fixture
def decimal_roman():
    with open('roman_numerals.csv', 'r') as f:
        return list(csv.DictReader(f))


def test_roman_1():
    assert 'I' == roman(1)

def test_roman_2():
    assert 'II' == roman(2)

def test_roman_3():
    assert 'III' == roman(3)

def test_roman_4():
    assert 'IV' == roman(4)

def test_roman_5():
    assert 'V' == roman(5)

def test_roman_6():
    assert 'VI' == roman(6)

def test_roman_7():
    assert 'VII' == roman(7)

def test_roman_8():
    assert 'VIII' == roman(8)

def test_roman_9():
    assert 'IX' == roman(9)

def test_roman_10():
    assert 'X' == roman(10)

def test_roman_50():
    assert 'L' == roman(50)

def test_roman_100():
    assert 'C' == roman(100)

def test_roman_500():
    assert 'D' == roman(500)

def test_roman_1000():
    assert 'M' == roman(1000)

def test_roman_exhaustive(decimal_roman):
    for item in decimal_roman:
        decimal = int(item['decimal'])
        assert item['roman'] == roman(decimal)
