from BST import BST
from BinaryTree import BinaryTree


class AVLTree(BST):
    """A class to extends the behavior so that the tree always stays balanced."""
    class AVLNode(BinaryTree.Node):
        """A class to extends the behavior of Node to fit for AVL requirements."""
        def __init__(self, value):
            super().__init__(value)
            self.parent = None
            self.height = 1

        def update_height(self):
            """Updates height field. A leaf height would defined as 1."""
            self.height = \
                max(0 if self.right is None else self.right.height,
                    0 if self.left is None else self.left.height) + 1

        @property
        def balance(self):
            """Evaluates height(right) - height(left). If te tree is balanced the result would be between -1 to 1."""
            return (0 if self.right is None else self.right.height) - (0 if self.left is None else self.left.height)

        def get_mostright_son(self):
            """:returns the most right son of the subroot. Apparently, the biggest value in the subtree."""
            if self.right is None:
                return self
            else:
                return self.right.get_mostright_son()

    def __init__(self):
        super().__init__()

    def insert(self, value):
        """Insert a value to the tree. If the tree is empty (meaning: self._root is None) - simply assigning self._root
        to a subroot with the value of ``value``, else - use the recursive method to insert the value down in the tree."""
        if self._root is None:
            self._root = AVLTree.AVLNode(value)
        else:
            self._root = self._insert(self._root, value)

    def delete(self, value):
        """Deletes the value ``value`` from the tree."""
        self._root = AVLTree._delete(self._root, value)

    def exist(self, value):
        """:returns True if value is in the tree,false otherwise."""
        return bool(AVLTree._find(self._root, value))

    def validate(self):
        """:returns True if the tree is validate as AVL (every subtree is balanced, and for every subroot -
        left is smaller and right is big or equal), false otherwise."""
        return super()._validate_subtree_order(self._root) and \
               self._validate_subtree_balance(self._root)

    @staticmethod
    def _insert(subroot, value):
        """Insert the value to the fit place in the subtree, then balance the tree (if required).
        :return returns the new subroot in order to maintaining the linking between the nodes in the tree."""
        subroot = AVLTree._insert_to_subtree(subroot, value)
        subroot = AVLTree.balance_subtree(subroot)

        return subroot

    @staticmethod
    def _insert_to_subtree(node, value):
        """Insert the value to the fit place in the subtree, so the tree stays BST.
        :returns the new subtree.
        :param node: subroot mustn't be None."""
        if value < node.value:
            if node.left is None:
                AVLTree.generate_son(node, value)
            else:
                node.left = AVLTree._insert(node.left, value)
        else:
            if node.right is None:
                AVLTree.generate_son(node, value)
            else:
                node.right = AVLTree._insert(node.right, value)

        return node

    @staticmethod
    def _delete(node, value):
        """Deletes a value from the tree. If the value does not exist in the tree, does nothing.
        if current value is value to delete, determines the current state, and according to it execute how to delete
        the value, else, search for its desire place in the tree. After deleting, balanced the tree bottom-up."""
        if node is not None:
            if value == node.value:
                if node.left is None and node.right is not None:
                    new_node = node.right

                    AVLTree.replace_node(node, new_node)

                    return new_node
                elif node.left is not None and node.right is None:
                    new_node = node.left

                    AVLTree.replace_node(node, new_node)

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
        return node

    @staticmethod
    def _find(node, value):
        """:returns a node from the tree with the required value if exit, None otherwise."""
        if node:
            if value == node.value:
                return node
            elif value < node.value:
                return AVLTree._find(node.left, value)
            else:
                return AVLTree._find(node.right, value)

    @staticmethod
    def replace_node(node, new_node):
        """Remove a node and connect a new node instead of it."""
        if node.parent:
            if node.parent.value < node.value:
                node.parent.right = new_node
            else:
                node.parent.left = new_node
            node.parent.update_height()
        if new_node is not None:
            new_node.parent = node.parent

    @staticmethod
    def balance_subtree(subroot):
        """If the subtree is unbalanced - balance the subtree.
        :returns the new subroot"""
        subroot.update_height()

        balance = subroot.balance

        if balance > 1:
            if subroot.right.balance < 0:
                subroot = AVLTree._rotate_rl(subroot)
            else:
                subroot = AVLTree._rotate_left(subroot)

        elif balance < -1:
            if subroot.left.balance < 0:
                subroot = AVLTree._rotate_right(subroot)
            else:
                subroot = AVLTree._rotate_lr(subroot)
        return subroot

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

    @staticmethod
    def _validate_subtree_balance(node):
        """:returns True if the subtree is (recursively) balanced, false otherwise."""
        if node:
            subtree_is_valid = AVLTree._validate_subtree_balance(node.left) and AVLTree._validate_subtree_balance(node.right)
            return subtree_is_valid and abs(node.balance) < 2
        return True



