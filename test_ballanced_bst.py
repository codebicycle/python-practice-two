from balanced_bst import build_balanced_tree


def test_ballanced_tree_from_collection():
    ordered = range(3, 13)
    bst = build_balanced_tree(ordered)
    assert 7 == bst.root.value
    assert 4 == bst.root.left.value
    assert 10 == bst.root.right.value
    assert 3 == bst.root.left.left.value
    assert 5 == bst.root.left.right.value
    assert 6 == bst.root.left.right.right.value
    assert 8 == bst.root.right.left.value
    assert 9 == bst.root.right.left.right.value
    assert 11 == bst.root.right.right.value
    assert 12 == bst.root.right.right.right.value
