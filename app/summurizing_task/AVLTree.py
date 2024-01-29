from BST import BST
from BinaryTree import BinaryTree


class AVLTree(BST):
    class AVLNode(BinaryTree.Node):

        def __init__(self, value):
            super().__init__(value)
            self.parent = None
            self.height = 1

        def update_height(self):
            self.height = \
                max(0 if self.right is None else self.right.height, 0 if self.left is None else self.left.height) + 1

        @property
        def height(self):
            return self._height

        @height.setter
        def height(self, height):
            self._height = height

        @property
        def balance(self):
            return (0 if self.right is None else self.right.height) - (0 if self.left is None else self.left.height)

        @staticmethod
        def get_height(node):
            if node is None:
                return 0
            return max(node.get_height(node.left), node.get_height(node.right)) + 1

    def __init__(self):
        super().__init__()

    def insert(self, value):
        if self._root is None:
            self._root = AVLTree.AVLNode(value)
        else:
            self._root = self._insert_to_node(value, self._root, AVLTree.AVLNode)

    @staticmethod
    def _insert_to_node(value, node, node_type = AVLNode):
        if value < node.value:
            if node.left is None:
                AVLTree.generate_son(node, value)
            else:
                node.left = AVLTree._insert_to_node(value, node.left, node_type)
        else:
            if node.right is None:
                AVLTree.generate_son(node, value)
            else:
                node.right = AVLTree._insert_to_node(value, node.right, node_type)
        node.update_height()
        balance = node.balance

        # Left Left Case
        if balance < -1 and value < node.left.value:
            return AVLTree._rotate_right(node)

        # Right Right Case
        if balance > 1 and value > node.right.value:
            return AVLTree._rotate_left(node);

        # Left Right Case
        if balance < -1 and value > node.left.value:
            node.left = AVLTree._rotate_left(node.left)
            return AVLTree._rotate_right(node)

        # Right Left Case
        if balance > 1 and value < node.right.value:
            node.right = AVLTree._rotate_right(node.right)
            return AVLTree._rotate_left(node)

        return node

    @staticmethod
    def _rotate_left(node):

        new_subroot = node.right

        AVLTree.connect_nodes(node, new_subroot.left)
        new_subroot.parent = node.parent
        if node.parent is not None:
            node.parent.right = new_subroot
        AVLTree.connect_nodes(new_subroot, node)

        return new_subroot

    @staticmethod
    def _rotate_right(node):

        new_subroot = node.left

        AVLTree.connect_nodes(node, new_subroot.right)
        new_subroot.parent = node.parent
        if node.parent is not None:
            node.parent.left = new_subroot
        AVLTree.connect_nodes(new_subroot, node)
        # update height -----------------------------------------------------------------------
        return new_subroot

    @staticmethod
    def generate_son(father, value, node_type = AVLNode):
        son = node_type(value)
        AVLTree.connect_nodes(father, son)

    @staticmethod
    def connect_nodes(father, son):
        if son is not None:
            son.parent = father
            if father.value > son.value:
                father.left = son
            else:
                father.right = son
        father.update_height()

