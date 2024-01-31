from BinaryTree import BinaryTree


class BST(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        if self._root is None:
            self._root = BinaryTree.Node(value)
        else:
            self._insert(value, self._root)

    @staticmethod
    def _insert(value, node, node_type = BinaryTree.Node):
        if value < node.value:
            if node.left is None:
                node.left = node_type(value)
            else:
                BST._insert(value, node.left, node_type)
        else:
            if node.right is None:
                node.right = node_type(value)
            else:
                BST._insert(value, node.right, node_type)
