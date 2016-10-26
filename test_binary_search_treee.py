import unittest
from binary_search_tree import BinarySearchTree

class BinarySearchTreeTest(unittest.TestCase):

    def test_bst_contains_returns_true_for_existing_value(self):
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(6)
        bst.add(3)
        bst.add(4)
        self.assertTrue(bst.contains(4))
        self.assertTrue(bst.contains(3))
        self.assertTrue(bst.contains(5))
        self.assertTrue(bst.contains(6))

    def test_bst_contains_returns_false_for_inexisting_value(self):
        bst = BinarySearchTree()
        bst.add(3)
        bst.add(1)
        bst.add(2)
        bst.add(4)
        self.assertFalse(bst.contains(5))
        self.assertFalse(bst.contains(6))
        self.assertFalse(bst.contains(99))
        self.assertFalse(bst.contains(0))
        self.assertFalse(bst.contains(-1))
