from advent_of_code_2016.day9 import parse


def test_parse():
    content = 'aaa(2x3)xyzzz'
    message = []
    parse(content, message)
    expected = ['aaa', 'xyxyxy', 'zzz']
    assert expected == message
