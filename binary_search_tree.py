
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = BinarySearchNode(value)
        else:
            self.root.add(value)

    def contains(self, target):
        node = self.root
        while node:
            if target == node.value:
                return True
            elif target < node.value:
                node = node.left
            else:
                node = node.right

        return False



class BinarySearchNode:
    def __init__(self, value = None):
        self.value  = value
        self.left   = None
        self.right  = None

    def add(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchNode(value)
            else:
                self.left.add(value)
        else:
            if self.right == None:
                self.right = BinarySearchNode(value)
            else:
                self.right.add(value)
