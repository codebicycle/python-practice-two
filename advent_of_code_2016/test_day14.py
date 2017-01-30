from advent_of_code_2016.day14 import md5_long


def test_md5_long():
    message = 'abc0'
    result = md5_long(message)
    expected = 'a107ff634856bb300138cac6568c0f24'
    assert expected == result
