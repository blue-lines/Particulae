__author__ = 'Julien'


import pymongo


class mongoDatabase:

    def __init__(self):
        # establish a connection to the database
        self.connection = pymongo.MongoClient("mongodb://localhost")
        self.db = self.connection.particulae
        self.collection = self.db.stock_data


    def insertStockData(self, collection_name, stock_data):
        self.db[collection_name].insert_one(stock_data)


