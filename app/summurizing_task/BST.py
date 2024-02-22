from BinaryTree import BinaryTree


class BST(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        """Insert a value to the tree. If the tree is empty (meaning: self._root is None) - simply assigning self._root
        to a subroot with the value of ``value``, else - use the recursive method to insert the value down in the tree."""
        if self._root is None:
            self._root = BinaryTree.Node(value)
        else:
            self._root = self._insert_to_BST(value, self._root)

    def validate(self):
        return self._validate_subtree()

    @staticmethod
    def _validate_subtree(node):
        if node:
            return (node.left.value < node.value if node.left else True) and \
                   (node.value <= node.right.value if node.right else True) and \
                    BST._validate_subtree(node.left) and BST._validate_subtree(node.right)
        return True
