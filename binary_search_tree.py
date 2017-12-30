class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def __contains__(self, target):
        node = self.root
        while node:
            if target == node.value:
                return True
            elif target < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def remove(self, value):
        if self.root:
            self.root = self.remove_from_parent(self.root, value)

    def remove_from_parent(self, parent, value):
        if parent is None:
            return None

        if value == parent.value:
            return parent.delete()
        elif value < parent.value:
            parent.left = self.remove_from_parent(parent.left, value)
        else:
            parent.right = self.remove_from_parent(parent.right, value)
        return parent

    def __str__(self):
        return str(self.root)

    def inorder(self):
        """In order traversal of elements from tree"""
        if self.root:
            return self.root.inorder()

    def preorder(self):
        if self.root:
            return self.root.preorder()

    def postorder(self):
        if self.root:
            return self.root.postorder()

    def __iter__(self):
        return self.inorder()


class BinaryNode:
    def __init__(self, value=None):
        self.value  = value
        self.left   = None
        self.right  = None

    def add(self, value):
        if value <= self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = BinaryNode(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinaryNode(value)

    def delete(self):
        """If this node would be removed from the tree, what node will take its place?
        Return the replacement node or None
        """
        if self.left is None and self.right is None:
            return None
        elif self.left is None:
            return self.right
        elif self.right is None:
            return self.left

        child = self.left
        if child.right:
            while child.right:
                parent = child
                child = child.right
            self.value = child.value
            parent.right = child.left
        else:
            self.left = child.left
            self.value = child.value
        return self

    def __repr__(self):
        return f'{self.value, self.left, self.right}'

    def inorder(self):
        if self.left:
            for value in self.left.inorder():
                yield value
        yield self.value
        if self.right:
            for value in self.right.inorder():
                yield value

    def preorder(self):
        yield self.value
        if self.left:
            for value in self.left.preorder():
                yield value
        if self.right:
            for value in self.right.preorder():
                yield value

    def postorder(self):
        if self.left:
            for value in self.left.postorder():
                yield value
        if self.right:
            for value in self.right.postorder():
                yield value
        yield self.value
