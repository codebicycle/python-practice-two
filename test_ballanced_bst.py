import math

from balanced_bst import build_balanced_tree


def test_ballanced_tree_from_collection():
    ordered = range(3, 13)
    bst = build_balanced_tree(ordered)
    max_height = math.log(len(ordered), 2)
    assert bst.height() <= max_height

    ordered = range(25_579)
    bst = build_balanced_tree(ordered)
    max_height = math.log(len(ordered), 2)
    assert bst.height() <= max_height
