from advent_of_code_2016.day18 import generate_tile, SAFE, TRAP


def test_generate_tile():
    assert SAFE == generate_tile('...')
    assert TRAP == generate_tile('..^')
    assert TRAP == generate_tile('.^^')
    assert TRAP == generate_tile('^^.')
    assert TRAP == generate_tile('^..')
    assert SAFE == generate_tile('^^^')
