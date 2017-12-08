from day5 import steps_to_exit, increment, decrement_or_increment

def test_examples():
    steps_count, state = steps_to_exit([0, 3, 0, 1, -3],
        update_callback=increment)
    assert 5 == steps_count
    assert [2, 5, 0, 1, -2] == state

