from advent_of_code_2016.day21 import (swap_position, swap_letter, rotate_right,
                                       rotate_left,
                                       rotate_based_on_letter_position,
                                       undo_rotate_based_on_letter_position,
                                       reverse_from, move)


def test_swap_position():
    chars = list('abc')
    result = swap_position(chars, '0', '2')
    assert list('cba') == result


def test_swap_letters():
    chars = list('aabcc')
    result = swap_letter(chars, 'a', 'c')
    assert list('ccbaa') == result


def test_rotate_left():
    chars = list('abcd')
    result = rotate_left(chars, '1')
    assert list('bcda') == result

    result = rotate_right(chars, '2')
    assert list('cdab') == result


def test_rotate_right():
    chars = list('abcd')

    result = rotate_right(chars, '1')
    assert list('dabc') == result


def test_rotate_based_on_letter_position():
    chars = list('abdec')
    result = rotate_based_on_letter_position(chars, 'b')
    assert list('ecabd') == result


def test_undo_rotate_based_on_letter_position():
    chars = list('abcdefgh')

    rotated = rotate_based_on_letter_position(chars, 'b')
    rotated_back = undo_rotate_based_on_letter_position(rotated, 'b')
    assert chars == rotated_back

    rotated = rotate_based_on_letter_position(chars, 'e')
    rotated_back = undo_rotate_based_on_letter_position(rotated, 'e')
    assert chars == rotated_back

    rotated = rotate_based_on_letter_position(chars, 'g')
    rotated_back = undo_rotate_based_on_letter_position(rotated, 'g')
    assert chars == rotated_back


def test_reverse_from():
    chars = list('..abc,,')
    result = reverse_from(chars, '2', '4')
    assert list('..cba,,') == result


def test_move():
    chars = list('abecedar')
    result = move(chars, '1', '4')
    assert list('aecebdar') == result
