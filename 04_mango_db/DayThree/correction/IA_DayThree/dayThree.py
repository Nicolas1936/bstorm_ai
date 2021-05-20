import pymongo
from models.authors import Author
from models.books import Book
from models.editors import Editor
from datetime import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["DayThree"]

books = mydb["books"]
authors = mydb["authors"]
editors = mydb["editors"]

nunn = Author(authors, "John", "Nunn")
print(nunn.__str__())

deFirmian = Author(authors, "Nick", "de Firmian")
deFirmian.birthdate = datetime.fromisoformat('1957-07-26')
print(deFirmian.toDictionary())
deFirmian.save()

batsford = Editor(editors, "023567", "Batsford")
print(batsford.__str__())
batsford.save()

bmco = Book(books, "147963", "Batsford's Modern chess openings")
bmco.addAuthor(deFirmian._id)
bmco.editor = batsford._id
print(bmco.__str__())
bmco.save()
batsford.addBook(bmco._id)
batsford.save()
deFirmian.addBook(bmco._id)
deFirmian.save()

mco = Book(books, "258741", "Modern Chess Opening")
rhpg = Editor(editors, "231854", "Random House Puzzles & Games")
rhpg.save()
mco.editor = rhpg._id
mco.addAuthor(deFirmian._id)
mco.save()
deFirmian.addBook(mco._id)
deFirmian.save()
rhpg.addBook(mco._id)
rhpg.save()

englishAttack = Book(books, "852654", "English Attack")
englishAttack.editor = batsford._id
englishAttack.addAuthor(deFirmian._id)
englishAttack.save()
deFirmian.addBook(englishAttack._id)
batsford.addBook(englishAttack._id)
deFirmian.save()
batsford.save()