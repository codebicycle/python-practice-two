from day4 import is_valid

def test_examples():
    assert True is is_valid('aa bb cc dd ee')
    assert False is is_valid('aa bb cc dd aa')
    assert True is is_valid('aa bb cc dd aaa')
