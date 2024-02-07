from abc import abstractmethod, ABC


class BinaryTree(ABC):
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
        pass

    def clear(self):
        self._root = None

    def get_in_order_values(self):
        return self._get_in_order_values(self._root)

    def get_pre_order_values(self):
        return self._get_pre_order_values(self._root)

    def get_post_order_values(self):
        return self._get_post_order_values(self._root)

    @staticmethod
    def _get_in_order_values(node, values_list = []):
        if node:
            BinaryTree._get_in_order_values(node.left, values_list)
            values_list.append(node.value)
            BinaryTree._get_in_order_values(node.right, values_list)
            return values_list

    @staticmethod
    def _get_pre_order_values(node, values_list = []):
        if node:
            values_list.append(node.value)
            BinaryTree._get_pre_order_values(node.left, values_list)
            BinaryTree._get_pre_order_values(node.right, values_list)
            return values_list

    @staticmethod
    def _get_post_order_values(node, values_list = []):
        if node:
            BinaryTree._get_post_order_values(node.left, values_list)
            BinaryTree._get_post_order_values(node.right, values_list)
            values_list.append(node.value)
            return values_list


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


