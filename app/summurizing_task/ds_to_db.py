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

        self.db = client[db_name]
        dwarfs = self.db[dwarfs_col_name]
        dwarfs_num = dwarfs.count_documents({})

        self.dwarf_name = dwarf_name

        field = 'name'
        query = {field: self.dwarf_name}
        if dwarfs.count_documents(query) == 0:
            new_dwarf = {'_id': dwarfs_num, field: self.dwarf_name}
            dwarfs.insert_one(new_dwarf)
        self.dwarf_col = self.db[self.dwarf_name]

        for treasure in self.dwarf_col.find({}, {'value': 1}): # complete
            super().insert(treasure['value'])

    def insert(self, value):
        if self.exist(value):
            return 400
        else:
            super().insert(value)
            treasure_id =  self.dwarf_col.count_documents({})
            treasure = {'_id': treasure_id, 'value': value}
            self.dwarf_col.insert_one(treasure)
            return 200

    def clear(self):
        self.dwarf_col.delete_many({})
        super().clear()
        return 200









