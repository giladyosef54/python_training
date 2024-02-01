import pymongo
import AVLTree


collections_metadata_col = 'dwarfs'
treasures_and_keepers_db = 'Treasures_and_keepers'
host_url = "mongodb://localhost:27017/"


class ds_to_db(AVLTree.AVLTree):
    def __init__(self, dwarf_name ='gilad_yosef',  # Collection of records
                 dwarfs_col_name = collections_metadata_col,
                 db_name = treasures_and_keepers_db,
                 bt_connection_string = host_url):

        super().__init__()

        client = pymongo.MongoClient(bt_connection_string)

        self._db = client[db_name]
        dwarfs = self._db[dwarfs_col_name]
        dwarfs_num = dwarfs.count_documents({})

        self._dwarf_name = dwarf_name

        field = 'name'
        query = {field: self._dwarf_name}
        if dwarfs.count_documents(query) == 0:
            new_dwarf = {'_id': dwarfs_num, field: self._dwarf_name}
            dwarfs.insert_one(new_dwarf)

        self._dwarf_col = self._db[self._dwarf_name]
        self._treasure_field = 'value'
        for treasure in self._dwarf_col.find({}, {self._treasure_field: 1}):
            super().insert(treasure[self._treasure_field])

    def insert(self, value):
        if self.exist(value):
            return 400
        else:
            super().insert(value)
            treasure_id = self._dwarf_col.count_documents({})
            treasure = {'_id': treasure_id, self._treasure_field: value}
            self._dwarf_col.insert_one(treasure)
            return 200

    def clear(self):
        self._dwarf_col.delete_many({})
        super().clear()
        return 200

    def delete(self, value):
        if not self.exist(value):
            return 400
        else:
            super().delete(value)

            treasure_query = {self._treasure_field: value}
            self._dwarf_col.delete_one(treasure_query)
            return 200

    def search_treasure(self, value):
        return 200 if self.exist(value) else 400

    def pre_order_traversal(self):
        values = self.get_pre_order_values()
        return values, 200

    def in_order_traversal(self):
        values = self.get_in_order_values()
        return values, 200

    def post_order_traversal(self):
        values = self.get_post_order_values()
        return values, 200

    def compare_ds_db(self):
        tree_values = set()
        for val in self:
            tree_values.add(val)

        db_treasures = set()
        for treasure in self._dwarf_col.find({}):
            db_treasures.add(treasure[self._treasure_field])

        if db_treasures == tree_values:
            return 200
        else:
            return 400









