from abc import abstractmethod, ABC
import pymongo


class BinaryTree(ABC):
    class Node:
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value

    def __init__(self):
        self._root = None

    def __iter__(self):
        return InOrderIterator(self._root)

    @abstractmethod
    def insert(self, value):
        pass

    def clear(self):
        self._root = None




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


