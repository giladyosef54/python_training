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
                max(0 if self.right is None else self.right.height,
                    0 if self.left is None else self.left.height) + 1

        @property
        def height(self):
            return self._height

        @height.setter
        def height(self, height):
            self._height = height

        @property
        def balance(self):
            return (0 if self.right is None else self.right.height) - (0 if self.left is None else self.left.height)

        def get_mostright_son(self):
            if self.right is None:
                return self
            else:
                return self.right.get_mostright_son()

    def __init__(self):
        super().__init__()

    def insert(self, value):
        if self._root is None:
            self._root = AVLTree.AVLNode(value)
        else:
            self._root = self._insert_to_node(value, self._root)

    def delete(self, value):
        self._root = AVLTree._delete(self._root, value)

    def exist(self, value):
        return bool(AVLTree._find(self._root, value))

    @staticmethod
    def _insert_to_node(value, node):
        if value < node.value:
            if node.left is None:
                AVLTree.generate_son(node, value)
            else:
                node.left = AVLTree._insert_to_node(value, node.left)
        else:
            if node.right is None:
                AVLTree.generate_son(node, value)
            else:
                node.right = AVLTree._insert_to_node(value, node.right)
        node.update_height()
        balance = node.balance

        # Left Left Case
        if balance < -1 and value < node.left.value:
            return AVLTree._rotate_right(node)

        # Right Right Case
        if balance > 1 and value > node.right.value:
            return AVLTree._rotate_left(node)

        # Left Right Case
        if balance < -1 and value > node.left.value:
            return AVLTree._rotate_lr(node)

        # Right Left Case
        if balance > 1 and value < node.right.value:
            return AVLTree._rotate_rl(node)

        return node

    @staticmethod
    def _delete(node, value):
        if node is not None:
            if value == node.value:
                if node.left is None and node.right is not None:
                    new_node = node.right

                    AVLTree.replace_node(node, new_node)

                    # new_node = AVLTree.balance_subtree(new_node)
                    return new_node
                elif node.left is not None and node.right is None:
                    new_node = node.left

                    AVLTree.replace_node(node, new_node)

                    # new_node = AVLTree.balance_subtree(new_node)
                    return new_node
                elif node.left is None and node.right is None:
                    new_node = None

                    AVLTree.replace_node(node, new_node)

                    return new_node
                else:
                    new_value = node.left.get_mostright_son().value
                    node.left = AVLTree._delete(node.left, new_value)
                    node.value = new_value

                    node = AVLTree.balance_subtree(node)
            elif value < node.value:
                node.left = AVLTree._delete(node.left, value)
                node = AVLTree.balance_subtree(node)
            elif value > node.value:
                node.right = AVLTree._delete(node.right, value)
                node = AVLTree.balance_subtree(node)
            node.update_height()
        return node

    @staticmethod
    def _find(node, value):
        if node:
            if value == node.value:
                return node
            elif value < node.value:
                return AVLTree._find(node.left, value)
            else:
                return AVLTree._find(node.right, value)

    @staticmethod
    def replace_node(node, new_node):
        if node.parent:
            if node.parent.value < node.value:
                node.parent.right = new_node
            else:
                node.parent.left = new_node
            node.parent.update_height()
        if new_node is not None:
            new_node.parent = node.parent

    @staticmethod
    def balance_subtree(root):
        left_height = 0 if root.left is None else root.left.height
        right_height = 0 if root.right is None else root.right.height

        if abs(left_height - right_height) == 2:
            if left_height < right_height:
                rl_height = 0 if root.right.left is None else root.right.left.height
                rr_height = 0 if root.right.right is None else root.right.right.height

                if rl_height > rr_height:
                    root = AVLTree._rotate_rl(root)
                else:
                    root = AVLTree._rotate_right(root)
            else:
                ll_height = 0 if root.left.left is None else root.left.left.height
                lr_height = 0 if root.left.right is None else root.left.right.height

                if ll_height > lr_height:
                    root = AVLTree._rotate_left(root)
                else:
                    root = AVLTree._rotate_lr(root)
        return root

    @staticmethod
    def _rotate_left(node):

        new_subroot = node.right

        node.right = new_subroot.left
        if new_subroot.left is not None:
            new_subroot.left.parent = node

        new_subroot.parent = node.parent

        new_subroot.left = node
        node.parent = new_subroot

        node.update_height()
        new_subroot.update_height()

        return new_subroot

    @staticmethod
    def _rotate_right(node):

        new_subroot = node.left

        node.left = new_subroot.right
        if new_subroot.right is not None:
            new_subroot.right.parent = node

        new_subroot.parent = node.parent

        new_subroot.right = node
        node.parent = new_subroot

        node.update_height()
        new_subroot.update_height()

        return new_subroot

    # Left right rotation.
    @staticmethod
    def _rotate_lr(node):
        node.left = AVLTree._rotate_left(node.left)
        return AVLTree._rotate_right(node)

    # Right left rotation.
    @staticmethod
    def _rotate_rl(node):
        node.right = AVLTree._rotate_right(node.right)
        return AVLTree._rotate_left(node)

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



