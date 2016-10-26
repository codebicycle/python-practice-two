
from binary_search_tree import BinarySearchTree

def gen_ballanced_bst(ordered):
    insertion_order = ballanced_bst_repr(ordered)
    bst = BinarySearchTree()
    for item in insertion_order:
        bst.add(item)

    return bst


def ballanced_bst_repr(ordered):
    low  = 0
    high = len(ordered) - 1
    mid = (low + high) // 2
    while low <= high:
        node  = ordered[mid]
        left  = ballanced_bst_repr(ordered[0     : mid])
        right = ballanced_bst_repr(ordered[mid+1 :    ])
        
        # bst = []
        # bst.append(node)
        # bst.append(left)
        # bst.append(right)
        # return bst

        bst = []
        bst.append(node)
        if left:
            bst += left
        if right:
            bst += right

        return bst
   
    return None
