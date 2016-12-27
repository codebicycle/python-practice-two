from advent_of_code_2016.day4 import is_valid, parse


def test_is_valid():
    name, _, checksum = parse('aaaaa-bbb-z-y-x-123[abxyz]')
    assert is_valid(name, checksum) is True

    name, _, checksum = parse('a-b-c-d-e-f-g-h-987[abcde]')
    assert is_valid(name, checksum) is True

    name, _, checksum = parse('not-a-real-room-404[oarel]')
    assert is_valid(name, checksum) is True

    name, _, checksum = parse('totally-real-room-200[decoy]]')
    assert is_valid(name, checksum) is False
