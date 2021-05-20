import pymongo
from bson import ObjectId
from datetime import datetime

class Author():
    def __str__(self) -> str:
        return str(self.toDictionary())

    def toDictionary(self):
        dico = {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "birthdate": self.birthdate,
            "books": self.books
        }
        return dico

    def save(self):
        if not self._id:
            self.collection.insert_one(self.toDictionary())
            author = self.collection.find_one({ "firstname": self.firstname, "lastname": self.lastname })
            self._id = author["_id"]
        else:
            self.collection.update_one({ "_id": self._id }, { "$set" : self.toDictionary() })

    def delete(self):
        if self._id:
            self.collection.find_one_and_delete({ "_id": self._id })

    def __init__(self, collection, firstname, lastname):
        self.collection = collection
        author = self.collection.find_one({ "firstname": firstname, "lastname": lastname })
        if author:
            self._id = author["_id"]
            self.firstname = author["firstname"]
            self.lastname = author["lastname"]
            self.birthdate = author["birthdate"]
            self.books = author["books"]
        else:
            self._id = 0
            self.firstname = firstname
            self.lastname = lastname
            self.birthdate = datetime.now()
            self.books = []

    def add_author(self):
        exist = self.collection.find_one({ "firstname": self.firstname, "lastname": self.lastname })
        if not exist:
            print('-----')
            print('creating Author...')
        else:
            print('Author already exist!')

