import pymongo
from pprint import pprint
from bson.json_util import dumps

from models.author import Author 
from models.editor import Editor
from models.book import Book

client = pymongo.MongoClient("mongodb+srv://nico:Nico_1936@cluster0.hs3hv.mongodb.net/test?retryWrites=true&w=majority")

db = client.mydb

authors = db.authors
editors = db.editors
books = db.books

nico_author = Author(authors, 'Nicolas', 'Blanchard')
nico_author.save()

kath_editor = Editor(editors, 'abcabcd', 'Kathleen Editor')
kath_editor.save()

bruxelles_book = Book(books, '1231232', 'Bruxelles: la ville')
bruxelles_book.editor = kath_editor._id
bruxelles_book.add_author(nico_author._id)
bruxelles_book.save()

nico_author.add_book(bruxelles_book._id)
nico_author.save()

kath_editor.add_book(bruxelles_book._id)
kath_editor.save()

bruxelles_book.delete()
nico_author.delete()
kath_editor.delete()