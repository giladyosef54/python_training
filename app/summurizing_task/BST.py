from BinaryTree import BinaryTree


class BST(BinaryTree):
    def __init__(self):
        super().__init__()

    def validate(self):
        return self._validate_subtree()

    @staticmethod
    def _validate_subtree(node):
        if node:
            return (node.left.value < node.value if node.left else True) and \
                   (node.value <= node.right.value if node.right else True) and \
                    BST._validate_subtree(node.left) and BST._validate_subtree(node.right)
        return True
