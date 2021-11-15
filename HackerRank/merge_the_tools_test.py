from merge_the_tools import merge_the_tools_helper


def test_merge_the_tools_helper():
    string = 'AABCAAADA'
    k = 3
    expected = ['AB', 'CA', 'AD']
    assert merge_the_tools_helper(string, k) == expected

    string = 'AAABCADDE'
    k = 3
    expected = ['A', 'BCA', 'DE']
    assert merge_the_tools_helper(string, k) == expected
