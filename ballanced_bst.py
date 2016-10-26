
from binary_search_tree import BinarySearchTree

def ballanced_tree(ordered):
    bt   = BinarySearchTree()
    low  = 0
    high = len(ordered) - 1
    add_range(bt, ordered, low, high)

    return bt


def add_range(bt, ordered, low, high):
    if low <= high:
        mid = (low + high) // 2

        bt.add(ordered[mid])
        add_range(bt, ordered, low, mid-1)
        add_range(bt, ordered, mid+1, high)
