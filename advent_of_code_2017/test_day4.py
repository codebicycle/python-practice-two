from day4 import no_duplicates, no_anagrams

def test_examples():
    assert True is no_duplicates('aa bb cc dd ee')
    assert False is no_duplicates('aa bb cc dd aa')
    assert True is no_duplicates('aa bb cc dd aaa')

def test_examples_part2():
    assert True is no_anagrams('abcde fghij')
    assert False is no_anagrams('abcde xyz ecdab')
    assert True is no_anagrams('a ab abc abd abf abj')
    assert True is no_anagrams('iiii oiii ooii oooi oooo')
    assert False is no_anagrams('oiii ioii iioi iiio')
