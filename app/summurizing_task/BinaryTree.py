from abc import abstractmethod, ABC
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


mydb = myclient["mydatabase"]


class BinaryTree(ABC):
    class Node():

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

    @abstractmethod
    def insert(self, value):
        pass



