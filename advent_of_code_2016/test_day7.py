from advent_of_code_2016.day7 import valid_ssl


def test_valid_ssl():
    assert valid_ssl('aba[bab]xyz') is True
    assert valid_ssl('xyx[xyx]xyx') is False
    assert valid_ssl('aaa[kek]eke') is True
    assert valid_ssl('zazbz[bzb]cdb') is True
    assert valid_ssl('abab[bab]') is True
