from advent_of_code_2016.day1 import Turtle


def test_get_distance_traveled():
    turtle = Turtle()
    turtle.travel('R2, R3')
    assert 5 == turtle.get_distance_traveled()

    turtle = Turtle()
    turtle.travel('R2, R2, R2')
    assert 2 == turtle.get_distance_traveled()

    turtle = Turtle()
    turtle.travel('R5, L5, R5, R3')
    assert 12 == turtle.get_distance_traveled()
