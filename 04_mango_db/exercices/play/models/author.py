import pymongo
from datetime import datetime
from bson import ObjectId

class Author:
    #INSERT AUTHOR
    def save(self):
        if self._id:
            self.collection.update_one(
                {'_id' : self._id}, 
                {'$set': self.to_dict()}
            )
        else:
            result = self.collection.insert_one(self.to_dict())
            self._id = ObjectId(result.inserted_id)
            print(result.inserted_id)

    #DELETE AUTHOR
    def delete(self):
        if self._id:
            self.collection.delete_one(self.to_dict())

    #ADD BOOK FOR THE AUTHOR
    def add_book(self, book_id):
        if book_id not in self.books:
            self.books.append(book_id)

    #MAKE A DICT FROM THE AUTHOR
    def to_dict(self, with_id=False):
        if with_id:
            dico = {
                '_id': self._id,
                'firstname': self.firstname,
                'lastname': self.lastname,
                'birthdate': self.birthdate,
                'books': self.books
            }
        else:
            dico = {
                'firstname': self.firstname,
                'lastname': self.lastname,
                'birthdate': self.birthdate,
                'books': self.books
            }
            
        return dico
    
    #INITIALISATION
    def __init__(self, collection, firstname, lastname):
        self.collection = collection
        
        search = {
            'firstname': firstname,
            'lastname': lastname
        }
        author = self.collection.find_one(search)
        
        if author:
            self._id = author['_id']
            self.firstname = author['firstname']
            self.lastname = author['lastname']
            self.birthdate = author['birthdate']
            self.books = author['books']
        else:
            self._id = 0
            self.firstname = firstname
            self.lastname = lastname
            self.birthdate = datetime(2000, 1, 1)
            self.books = []

    #TO STRING
    def __str__(self):
        return str(self.to_dict(True))