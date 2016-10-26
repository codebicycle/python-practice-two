from binary_search import *
import unittest

class BinarySearchTest(unittest.TestCase):

    def setUp(self):
        self.collection = [11,12,13,14,15,16,17,18,19]

    def test_bs_contains_target_element(self):
        self.assertTrue(bs_contains(self.collection, 13))
        self.assertTrue(bs_contains(self.collection, 11))
        self.assertTrue(bs_contains(self.collection, 19))
        self.assertTrue(bs_contains(self.collection, 18))

    def test_bs_does_not_contain_target_element(self):
        self.assertFalse(bs_contains(self.collection,  5))
        self.assertFalse(bs_contains(self.collection, -1))
        self.assertFalse(bs_contains(self.collection,  0))
        self.assertFalse(bs_contains(self.collection, 99))
        self.assertFalse(bs_contains(self.collection, 20))

    def test_binary_search_correct_position_when_target_found(self):
        self.assertEquals(2 ,binary_search(self.collection, 13))
        self.assertEquals(0 ,binary_search(self.collection, 11))
        self.assertEquals(8 ,binary_search(self.collection, 19))
        self.assertEquals(7 ,binary_search(self.collection, 18))

    def test_binary_search_when_target_not_in_collection(self):
        self.assertEquals(-1 ,binary_search(self.collection,  5))
        self.assertEquals(-1 ,binary_search(self.collection, -1))
        self.assertEquals(-1 ,binary_search(self.collection,  0))
        self.assertEquals(-1 ,binary_search(self.collection, 99))
