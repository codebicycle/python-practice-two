from advent_of_code_2016.day2 import get_code, KEYPAD_CLASSIC


def test_get_code():
    assert '1985' == get_code('ULL\nRRDDD\nLURDL\nUUUUD', KEYPAD_CLASSIC)
