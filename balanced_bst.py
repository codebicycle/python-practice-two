from binary_search_tree import BinarySearchTree

# Solution 1
def build_balanced_tree(ordered):
    bst = BinarySearchTree()
    low = 0
    high = len(ordered) - 1
    add_range(bst, ordered, low, high)
    return bst

def add_range(bst, ordered, low, high):
    if low <= high:
        mid = (low + high) // 2

        bst.add(ordered[mid])
        add_range(bst, ordered, low, mid-1)
        add_range(bst, ordered, mid+1, high)

# Solution 2
def build_balanced_tree(ordered):
    """Build a ballanced binary search tree from an ordered collection."""
    bst = BinarySearchTree()
    add(bst, ordered)
    return bst

def split(ordered):
    """Split sequence on median.
    Return a tuple containing: a list with the values from the left of the median,
    the median and another list with the values from the right of the median.
    """
    middle = (len(ordered) - 1) // 2
    left = ordered[:middle]
    median = ordered[middle]
    right = ordered[middle+1:]
    return left, median, right

def add(bst, ordered):
    left, median, right = split(ordered)
    bst.add(median)
    if left:
        add(bst, left)
    if right:
        add(bst, right)
