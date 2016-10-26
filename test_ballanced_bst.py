
import unittest
from ballanced_bst import *

class BallancedTreeTest(unittest.TestCase):

    def test_ballanced_tree_from_collection(self):
        ordered = range(3, 13)
        bt = ballanced_tree(ordered)
        self.assertEqual( 7, bt.root.value)
        self.assertEqual( 4, bt.root.left.value)
        self.assertEqual(10, bt.root.right.value)
        self.assertEqual( 3, bt.root.left.left.value)
        self.assertEqual( 5, bt.root.left.right.value)
        self.assertEqual( 6, bt.root.left.right.right.value)
        self.assertEqual( 8, bt.root.right.left.value)
        self.assertEqual( 9, bt.root.right.left.right.value)
        self.assertEqual(11, bt.root.right.right.value)
        self.assertEqual(12, bt.root.right.right.right.value)
