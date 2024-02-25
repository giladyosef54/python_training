import pymongo


class MongoCollectionManager:
    """A class to manage a collection in mongodb."""
    def __init__(self, connect_str, database_name, col_name):

        client = pymongo.MongoClient(connect_str)
        self._col = client[database_name][col_name]
        self._id_gen = self._col.count_documents({})

    def get_field(self, field_name):
        return [document[field_name] for document in self._col.find({}, {field_name: 1})]

    def get_values(self):
        return self.get_field('value')

    def insert_doc(self, query):
        query['_id'] = self._id_gen
        self._id_gen += 1
        self._col.insert_one(query)

    def insert_value(self, value):
        self._col.insert_one({'value': value})

    def clear_col(self):
        self._col.delete_many({})

    def delete_doc(self, query):
        self._col.delete_one(query)

    def delete_value(self, value):
        self.delete_doc({'value': value})




