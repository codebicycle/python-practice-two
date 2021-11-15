from most_commons import most_common_letters


def test_most_common_letters():
    text = 'GOOGLE'
    expected = [('G', 2), ('O', 2), ('E', 1)]
    assert most_common_letters(text) == expected
