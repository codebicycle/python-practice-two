from day1 import solve_captcha

def test_examples():
    assert 3 == solve_captcha(1122)
    assert 4 == solve_captcha(1111)
    assert 0 == solve_captcha(1234)
    assert 9 == solve_captcha(91212129)
