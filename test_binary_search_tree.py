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


def test_bst_remove():
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(6)
    bst.add(1)
    bst.add(4)
    bst.add(3)
    bst.remove(5)
    assert 5 not in bst
    assert bst.root.value == 4
    bst.remove(3)
    assert 3 not in bst
    bst.remove(6)
    assert 6 not in bst
    bst.remove(1)
    assert 1 not in bst
    bst.remove(4)
    assert 4 not in bst
    assert bst.root is None
