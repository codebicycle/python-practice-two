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


def test_bst_traversals():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(2)
    bst.add(5)
    bst.add(1)
    bst.add(3)
    inorder = bst.inorder()
    preorder = bst.preorder()
    postorder = bst.postorder()
    assert [1, 2, 3, 4, 5] == list(inorder)
    assert [4, 2, 1, 3, 5] == list(preorder)
    assert [1, 3, 2, 5, 4] == list(postorder)


def test_bst_height():
    bst = BinarySearchTree()
    assert bst.height() == None
    bst.add(5)
    assert bst.height() == 0
    bst.add(2)
    bst.add(7)
    assert bst.height() == 1
    bst.add(8)
    assert bst.height() == 2
    bst.add(9)
    assert bst.height() == 3
