from pymongo import MongoClient
from collections import OrderedDict

class dbConnection:
    def connection_start(self):
        self.mongo = MongoClient('mongodb://localhost:27017/')
        db = self.mongo.twitter
        try:
            if "twitter" in db.list_collection_names():
                query = [('collMod', 'twitter')]
                query = OrderedDict(query)
                db.command(query)
            else:
                db.create_collection("twitter")
        except Exception as e:
            print(e)
        return db

    def connection_close(self):
        self.mongo.close()
        return True