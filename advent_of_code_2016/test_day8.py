from advent_of_code_2016.day8 import Screen


def test_screen():
    screen = Screen(5, 3)
    assert 5 == screen.columns
    assert 3 == screen.rows
    assert 3 == len(screen.screen)
    assert 5 == len(screen.screen[0])
    assert Screen.OFF == screen.screen[0][0]

    screen.rectangle(1, 2)
    assert Screen.ON == screen.screen[0][0]
    assert Screen.ON == screen.screen[1][0]
    assert Screen.OFF == screen.screen[2][0]
    assert Screen.OFF == screen.screen[0][1]

    assert 2 == screen.count_lit_pixels()

