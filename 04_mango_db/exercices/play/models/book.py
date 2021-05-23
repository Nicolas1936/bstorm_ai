import pymongo
from datetime import datetime
from bson import ObjectId

class Book:
    #INSERT BOOK
    def save(self):
        if self._id:
            self.collection.update_one(
                {'_id' : self._id}, 
                {'$set': self.to_dict()}
            )
        else:
            print(self.to_dict())
            result = self.collection.insert_one(self.to_dict())
            self._id = ObjectId(result.inserted_id)

    #DELETE BOOK
    def delete(self):
        if self._id:
            self.collection.delete_one(self.to_dict())

    #ADD BOOK FOR THE AUTHOR
    def add_author(self, author_id):
        if author_id not in self.authors:
            self.authors.append(author_id)

    #MAKE A DICT FROM THE BOOK
    def to_dict(self, with_id=False):
        if with_id:
            dico = {
                '_id': self._id,
                'isbn': self.isbn,
                'title': self.title,
                'releaseDate': self.releaseDate,
                'authors': self.authors,
                'editor': self.editor
            }
        else:
            dico = {
                'isbn': self.isbn,
                'title': self.title,
                'releaseDate': self.releaseDate,
                'authors': self.authors,
                'editor': self.editor
            }
            
        return dico
    
    #INITIALISATION
    def __init__(self, collection, isbn, title):
        self.collection = collection
        
        search = {
            'isbn': isbn,
            'title': title
        }
        book = self.collection.find_one(search)
        
        if book:
            self._id = book['_id']
            self.isbn = book['isbn']
            self.title = book['title']
            self.releaseDate = book['releaseDate']
            self.authors = book['authors']
            self.editor = book['editor']
        else:
            self._id = 0
            self.isbn = isbn
            self.title = title
            self.releaseDate = datetime.now()
            self.authors = []
            self.editor = None

    #TO STRING
    def __str__(self):
        return str(self.to_dict(True))