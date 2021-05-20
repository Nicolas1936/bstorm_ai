import pymongo
from bson import ObjectId
from datetime import datetime

class Book():
    def __str__(self) -> str:
        return str(self.toDictionary())

    def toDictionary(self):
        dico = {
            "isbn": self.isbn,
            "title": self.title,
            "releaseDate": self.releaseDate,
            "authors": self.authors,
            "editor": self.editor
        }
        return dico

    def save(self):
        if not self._id:
            self.collection.insert_one(self.toDictionary())
            book = self.collection.find_one({ "isbn": self.isbn, "title": self.title })
            self._id = book["_id"]
        else:
            self.collection.update_one({ "_id": self._id }, { "$set" : self.toDictionary() })

    def delete(self):
        if self._id:
            self.collection.find_one_and_delete({ "_id": self._id })

    def __init__(self, collection, isbn, title):
        self.collection = collection
        book = self.collection.find_one({ "isbn": isbn, "title": title })
        if book:
            self._id = book["_id"]
            self.isbn = book["isbn"]
            self.title = book["title"]
            self.releaseDate = book["releaseDate"]
            self.authors = book["authors"]
            self.editor = book["editor"]
        else:
            self._id = 0
            self.isbn = isbn
            self.title = title
            self.releaseDate = datetime.now()
            self.authors = []
            self.editor = ''