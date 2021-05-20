import pymongo
from bson import ObjectId
from datetime import datetime

class Editor():
    def __str__(self) -> str:
        return str(self.toDictionary())

    def toDictionary(self):
        dico = {
            "NbrTVA": self.NbrTVA,
            "name": self.name,
            "creationDate": self.creationDate,
            "books": self.books
        }
        return dico

    def save(self):
        if not self._id:
            self.collection.insert_one(self.toDictionary())
            editor = self.collection.find_one({ "NbrTVA": self.NbrTVA, "name": self.name })
            self._id = editor["_id"]
        else:
            self.collection.update_one({ "_id": self._id }, { "$set" : self.toDictionary() })

    def delete(self):
        if self._id:
            self.collection.find_one_and_delete({ "_id": self._id })

    def __init__(self, collection, NbrTVA, name):
        self.collection = collection
        editor = self.collection.find_one({ "NbrTVA": NbrTVA, "name": name })
        if editor:
            self._id = editor["_id"]
            self.NbrTVA = editor["NbrTVA"]
            self.name = editor["name"]
            self.creationDate = editor["creationDate"]
            self.books = editor["books"]
        else:
            self._id = 0
            self.NbrTVA = NbrTVA
            self.name = name
            self.craetionDate = datetime.now()
            self.books = []