from day3 import distance_to_center

def test_examples():
    assert 0 == distance_to_center(1)
    assert 3 == distance_to_center(12)
    assert 2 == distance_to_center(23)
    assert 31 == distance_to_center(1024)
