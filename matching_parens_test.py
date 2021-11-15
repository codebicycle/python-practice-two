from matching_parens import matching_parens


def test_matching_parens():
    distinct = '[](){}<>'
    assert matching_parens(distinct)

    nested = '[(<{}>)]'
    assert matching_parens(nested)

    with_text = '{hello}<world>(!)'
    assert matching_parens(with_text)

    unclosed = '[()'
    assert matching_parens(unclosed) is False

    unmatched = '[(])'
    assert matching_parens(unmatched) is False

    back_to_back = '(><)'
    assert matching_parens(back_to_back) is False
