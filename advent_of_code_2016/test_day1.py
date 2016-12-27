from advent_of_code_2016.day1 import Turtle, get_first_duplicate


def test_get_distance_traveled():
    turtle = Turtle()
    turtle.travel('R2, R3')
    assert 5 == turtle.get_distance()

    turtle = Turtle()
    turtle.travel('R2, R2, R2')
    assert 2 == turtle.get_distance()

    turtle = Turtle()
    turtle.travel('R5, L5, R5, R3')
    assert 12 == turtle.get_distance()

    turtle = Turtle()
    turtle.travel('L9, L1')
    assert 10 == turtle.get_distance()


def test_get_distance_first_visit_twice():
    turtle = Turtle()
    turtle.travel('R8, R4, R4, R8')
    assert 4 == turtle.get_distance_first_visit_twice()

    turtle = Turtle()
    turtle.travel('L5, R1, R4, L5, L4, R3, R1, L1, R4, R5, L1, L3, R4, L2, L4, R2, L4, L1, R3, R1, R1, L1, R1, L5, R5, R2, L5, R2, R1, L2, L4, L4, R191, R2, R5, R1, L1, L2, R5, L2, L3, R4, L1, L1, R1, R50, L1, R1, R76, R5, R4, R2, L5, L3, L5, R2, R1, L1, R2, L3, R4, R2, L1, L1, R4, L1, L1, R185, R1, L5, L4, L5, L3, R2, R3, R1, L5, R1, L3, L2, L2, R5, L1, L1, L3, R1, R4, L2, L1, L1, L3, L4, R5, L2, R3, R5, R1, L4, R5, L3, R3, R3, R1, R1, R5, R2, L2, R5, L5, L4, R4, R3, R5, R1, L3, R1, L2, L2, R3, R4, L1, R4, L1, R4, R3, L1, L4, L1, L5, L2, R2, L1, R1, L5, L3, R4, L1, R5, L5, L5, L1, L3, R1, R5, L2, L4, L5, L1, L1, L2, R5, R5, L4, R3, L2, L1, L3, L4, L5, L5, L2, R4, R3, L5, R4, R2, R1, L5')
    assert 150 == turtle.get_distance_first_visit_twice()


def test_get_first_duplicate():
    locations = [(0, 1), (1, 1), (1, 1), (0, 1), ]
    assert (1, 1) == get_first_duplicate(locations)
