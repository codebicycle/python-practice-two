from advent_of_code_2016.day9 import parse_recursive, decode, decode_deep


def test_parse_recursive():
    content = 'aaa(2x3)xyzzz'
    message = []
    parse_recursive(content, message)
    expected = ['aaa', 'xyxyxy', 'zzz']
    assert expected == message


def test_decode():
    result = decode('ADVENT')
    expected = 'ADVENT'
    assert expected == result

    result = decode('A(1x5)BC')
    expected = 'ABBBBBC'
    assert expected == result

    result = decode('(3x3)XYZ')
    expected = 'XYZXYZXYZ'
    assert expected == result

    result = decode('A(2x2)BCD(2x2)EFG')
    expected = 'ABCBCDEFEFG'
    assert expected == result

    result = decode('(6x1)(1x3)A')
    expected = '(1x3)A'
    assert expected == result

    result = decode('X(8x2)(3x3)ABCY')
    expected = 'X(3x3)ABC(3x3)ABCY'
    assert expected == result


def test_decode_deep():
    content = '(3x3)XYZ'
    message, length = decode_deep(content)
    expected = 'XYZXYZXYZ'
    assert expected == message

    content = 'X(8x2)(3x3)ABCY'
    message, length = decode_deep(content)
    expected = 'XABCABCABCABCABCABCY'
    assert expected == message

    content = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
    message, length = decode_deep(content)
    expected = 'A' * 241920
    assert expected == message

    content = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
    message, length = decode_deep(content)
    assert 445 == length
