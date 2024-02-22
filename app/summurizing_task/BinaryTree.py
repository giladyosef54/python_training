from abc import abstractmethod, ABC


class BinaryTree(ABC):
    """An abstract class to represent and implement a binary tree data structure. Notice that the user shouldn't access
    to node objects, and treat the behinds of the class as black box."""
    class Node:
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

    def __init__(self):
        self._root = None

    def __iter__(self):
        return InOrderIterator(self._root)

    @abstractmethod
    def insert(self, value):
        """Inserts a value to the tree. Must be implemented in inherits class."""
        pass

    def clear(self):
        """Clears the tree of all its values."""
        self._root = None

    def get_in_order_values(self):
        """:returns a list with all the values of the tree in format of:
        [``subroot.left``, ``subroot.value``, ``subroot.right``]"""
        return self._get_in_order_values(self._root)

    def get_pre_order_values(self):
        """:returns a list with all the values of the tree in format of:
        [``subroot.value``, ``subroot.left``, ``subroot.right``]"""
        return self._get_pre_order_values(self._root)

    def get_post_order_values(self):
        """:returns a list with all the values of the tree in format of:
        [``subroot.left``, ``subroot.right``, ``subroot.value``]"""
        return self._get_post_order_values(self._root)

    def get_visualized_tree(self):
        """:returns a str that visualized the hierarchy in the tree"""
        return self._get_visualized_tree(self._root)

    @staticmethod
    def _get_in_order_values(subroot, values_list = []):
        """:returns a list with all the values under ``subroot`` in format of:
        [``subroot.left``, ``subroot.value``, ``subroot.right``]"""
        if subroot:
            BinaryTree._get_in_order_values(subroot.left, values_list)
            values_list.append(subroot.value)
            BinaryTree._get_in_order_values(subroot.right, values_list)
            return values_list

    @staticmethod
    def _get_pre_order_values(subroot, values_list = []):
        """:returns a list with all the values under ``subroot`` in format of:
        [``subroot.value``, ``subroot.left``, ``subroot.right``]"""
        if subroot:
            values_list.append(subroot.value)
            BinaryTree._get_pre_order_values(subroot.left, values_list)
            BinaryTree._get_pre_order_values(subroot.right, values_list)
        return values_list

    @staticmethod
    def _get_post_order_values(subroot, values_list = []):
        """:returns a list with all the values under ``subroot`` in format of:
        [``subroot.left``, ``subroot.right``, ``subroot.value``]"""
        if subroot:
            BinaryTree._get_post_order_values(subroot.left, values_list)
            BinaryTree._get_post_order_values(subroot.right, values_list)
            values_list.append(subroot.value)
            return values_list

    @staticmethod
    def _get_visualized_tree(node, level = 0):
        """:returns a str that visualized the hierarchy under node"""
        if node:
            visual = '--' * level + str(node.value) + '\n'
            visual += BinaryTree._get_visualized_tree(node.left, level + 1)
            visual += BinaryTree._get_visualized_tree(node.right, level + 1)
            return visual
        else: return ''


class InOrderIterator:

    def __init__(self, root):
        self.traversal = []
        self.move_left(root)

    def move_left(self, current):
        while current is not None:
            self.traversal.append(current)
            current = current.left

    def has_next(self):
        return len(self.traversal) > 0

    def __next__(self):
        if not self.has_next():
            raise StopIteration()

        current = self.traversal.pop()

        if current.right is not None:
            self.move_left(current.right)

        return current.value


