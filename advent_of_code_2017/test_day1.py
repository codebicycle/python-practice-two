from day1 import solve_captcha, solve_captcha_circular

def test_examples():
    assert 3 == solve_captcha(1122)
    assert 4 == solve_captcha(1111)
    assert 0 == solve_captcha(1234)
    assert 9 == solve_captcha(91212129)


def test_examples_part2():
    assert 6 == solve_captcha_circular(1212)
    assert 0 == solve_captcha_circular(1221)
    assert 4 == solve_captcha_circular(123425)
    assert 12 == solve_captcha_circular(123123)
    assert 4 == solve_captcha_circular(12131415)
