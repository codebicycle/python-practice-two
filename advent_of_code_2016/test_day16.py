from advent_of_code_2016.day16 import (dragon_curve_helper, dragon_curve,
                                       partition, get_checksum)


def test_dragon_curve_helper():
    assert '100' == dragon_curve_helper('1')
    assert '001' == dragon_curve_helper('0')

    string = '11111'
    result = dragon_curve_helper(string)
    expected = '11111000000'
    assert expected == result

    string = '111100001010'
    result = dragon_curve_helper(string)
    expected = '1111000010100101011110000'
    assert expected == result


def test_partitions():
    sequence = 'abcdefgh'
    partitions = partition(sequence, 2)
    expected = ['ab', 'cd', 'ef', 'gh']
    assert expected == partitions

    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
    partitions = partition(sequence, 2)
    expected = [[1, 2], [3, 4], [5, 6], [7, 8], [9]]
    assert expected == partitions


def test_get_checksum():
    puzzle_input = '10000'
    disk_size = 20

    data = dragon_curve(puzzle_input, disk_size)
    disk_data = data[:disk_size]
    checksum = get_checksum(disk_data)
    expected = '01100'
    assert expected == checksum
