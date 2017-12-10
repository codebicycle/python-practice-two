from day10 import hash_multiple, parse_bytes

def test_multiple_hash_examples():
    numbers = list(range(256))

    lengths = parse_bytes('')
    assert 'a2582a3a0e66e6e86e3812dcb672a272' == hash_multiple(numbers, lengths)

    lengths = parse_bytes('AoC 2017')
    assert '33efeb34ea91902bb2f59c9920caa6cd' == hash_multiple(numbers, lengths)

    lengths = parse_bytes('1,2,3')
    assert '3efbe78a8d82f29979031a4aa0b16a9d' == hash_multiple(numbers, lengths)

    lengths = parse_bytes('1,2,4')
    assert '63960835bcdc130f0b66d7ff4f6a5a8e' == hash_multiple(numbers, lengths)
