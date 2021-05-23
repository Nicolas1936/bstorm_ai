import pymongo
from datetime import datetime
from bson import ObjectId

class Editor:
    #INSERT EDITOR
    def save(self):
        if self._id:
            self.collection.update_one(
                {'_id' : self._id}, 
                {'$set': self.to_dict()}
            )
        else:
            result = self.collection.insert_one(self.to_dict())
            self._id = ObjectId(result.inserted_id)

    #DELETE EDITOR
    def delete(self):
        if self._id:
            self.collection.delete_one(self.to_dict())

    #ADD BOOK FOR THE EDITOR
    def add_book(self, book_id):
        if book_id not in self.books:
            self.books.append(book_id)

    #MAKE A DICT FROM THE EDITOR
    def to_dict(self, with_id=False):
        if with_id:
            dico = {
                '_id': self._id,
                'nbrTVA': self.nbrTVA,
                'name': self.name,
                'creationDate': self.creationDate,
                'books': self.books
            }
        else:
            dico = {
                'nbrTVA': self.nbrTVA,
                'name': self.name,
                'creationDate': self.creationDate,
                'books': self.books
            }
            
        return dico
    
    #INITIALISATION
    def __init__(self, collection, nbrTVA, name):
        self.collection = collection
        
        search = {
            'nbrTVA': nbrTVA,
            'name': name
        }
        editor = self.collection.find_one(search)
        
        if editor:
            self._id = editor['_id']
            self.nbrTVA = editor['nbrTVA']
            self.name = editor['name']
            self.creationDate = editor['creationDate']
            self.books = editor['books']
        else:
            self._id = 0
            self.nbrTVA = nbrTVA
            self.name = name
            self.creationDate = datetime.now()
            self.books = []

    #TO STRING
    def __str__(self):
        return str(self.to_dict(True))