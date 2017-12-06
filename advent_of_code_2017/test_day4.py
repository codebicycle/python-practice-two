from day4 import no_duplicates, no_anagrams

def test_examples():
    assert True is no_duplicates('aa bb cc dd ee'.split())
    assert False is no_duplicates('aa bb cc dd aa'.split())
    assert True is no_duplicates('aa bb cc dd aaa'.split())

def test_examples_part2():
    assert True is no_anagrams('abcde fghij'.split())
    assert False is no_anagrams('abcde xyz ecdab'.split())
    assert True is no_anagrams('a ab abc abd abf abj'.split())
    assert True is no_anagrams('iiii oiii ooii oooi oooo'.split())
    assert False is no_anagrams('oiii ioii iioi iiio'.split())
