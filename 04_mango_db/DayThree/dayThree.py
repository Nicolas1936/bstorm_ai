from models.book import Book
from models.editor import Editor
import pymongo
from models.author import Author

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient['DayThree']

authors = mydb["authors"]
editors = mydb["editors"]
books = mydb["books"]

hugo = Author(authors, 'Victor', 'Hugo')
print(hugo)

nicolasblanchard = Editor(editors, 'abc123', 'Nicolas Blanchard')
print(nicolasblanchard)

alchemiste = Book(books, '12345', 'alchemiste')
print(alchemiste)

print('###############')

hugo.add_author()

hugo.firstname = "kath"

hugo.add_author()