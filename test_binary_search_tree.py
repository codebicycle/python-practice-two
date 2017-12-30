from binary_search_tree import BinarySearchTree

def test_bst_contains_for_existing_values():
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(6)
    bst.add(3)
    bst.add(4)
    assert 4 in bst
    assert 3 in bst
    assert 5 in bst
    assert 6 in bst

def test_bst_contains_for_inexisting_values():
    bst = BinarySearchTree()
    bst.add(3)
    bst.add(1)
    bst.add(2)
    bst.add(4)
    assert 5 not in bst
    assert 6 not in bst
    assert 99 not in bst
    assert 0 not in bst
    assert -1 not in bst
