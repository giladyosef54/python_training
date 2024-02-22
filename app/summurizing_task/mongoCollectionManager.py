import pymongo


class MongoCollectionManager:
    def __init__(self, connect_str, database_name, col_name):
        client = pymongo.MongoClient(connect_str)
        self._col = client[database_name][col_name]

    def get_field(self, field_name):
        return [document[field_name] for document in self._col.find({}, {field_name: 1})]

    def get_values(self):
        return self.get_field('value')






