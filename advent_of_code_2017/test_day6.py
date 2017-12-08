from day6 import count_cycles

def test_examples():
    cycles, cycles_in_loop, state = count_cycles([0, 2, 7, 0])
    assert 5 == cycles
    assert [2, 4, 1, 2] == state
    assert 4 == cycles_in_loop
