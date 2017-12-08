from day5 import steps_to_exit

def test_examples():
    steps_count, state = steps_to_exit([0, 3, 0, 1, -3])
    assert 5 == steps_count
    assert [2, 5, 0, 1, -2] == state
