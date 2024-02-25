import pymongo
from mongoCollectionManager import MongoCollectionManager
from dotenv import load_dotenv
import AVLTree

load_dotenv()


TREASURES_AND_KEEPERS_DB = os.getenv("DATA_BASE")
HOST_URL = os.getenv("URL")


class MongoBackedAVL(AVLTree.AVLTree):
    def __init__(self, dwarf_name = 'gilad_yosef',
                 database_name = TREASURES_AND_KEEPERS_DB,
                 connect_str = HOST_URL):

        super().__init__()
        self._treasures = MongoCollectionManager(connect_str, database_name, dwarf_name)

        for treasure in self._treasures.get_values():
            super().insert(treasure)

    def insert(self, value):
        if self.exist(value):
            raise ValueError('Value already exist, can\'t insert.')
        else:
            super().insert(value)
            self._treasures.insert_value(value)

    def clear(self):
        self._treasures.clear_col()
        super().clear()

    def delete(self, value):
        if not self.exist(value):
            raise ValueError("Value not found.")
        else:
            super().delete(value)
            self._treasures.delete_value(value)

    def search_treasure(self, value):
        return self.exist(value)

    def pre_order_traversal(self):
        values = self.get_pre_order_values()
        return values

    def in_order_traversal(self):
        values = self.get_in_order_values()
        return values

    def post_order_traversal(self):
        values = self.get_post_order_values()
        return values

    def validate(self):
        return self._validate_subtree_order(self._root) and \
               super()._validate_subtree_balance(self._root)

    @staticmethod
    def _validate_subtree_order(node):
        if node:
            return (node.left.value < node.value if node.left else True) and \
                   (node.value < node.right.value if node.right else True) and \
                   MongoBackedAVL._validate_subtree_order(node.left) and MongoBackedAVL._validate_subtree_order(node.right)
        return True









