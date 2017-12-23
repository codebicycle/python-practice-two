from day22 import Grid


def test_grid_turn_left():
    grid = Grid()
    assert grid.NORTH == grid.direction

    grid._turn_left()
    assert grid.WEST == grid.direction

    grid._turn_left()
    assert grid.SOUTH == grid.direction

    grid._turn_left()
    assert grid.EAST == grid.direction

    grid._turn_left()
    assert grid.NORTH == grid.direction


def test_grid_turn_right():
    grid = Grid()
    assert grid.NORTH == grid.direction

    grid._turn_right()
    assert grid.EAST == grid.direction

    grid._turn_right()
    assert grid.SOUTH == grid.direction

    grid._turn_right()
    assert grid.WEST == grid.direction

    grid._turn_right()
    assert grid.NORTH == grid.direction
