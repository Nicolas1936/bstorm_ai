
from models.user import Users
from models.book import Books
from models.editor import Editor

import pymongo


# CONNECT TO THE DATABASE
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# GET ALL THE DATABASE
dblist = myclient.list_database_names()

for db in dblist:
    print(db)

# CREATE OR TAKE THE DATABASE "Example_IA"
mydb = myclient["Example_IA"]
if "Example_IA" in dblist:
    print("database already exist!")

print("initialize data...")

# CREATE COLLECTIONS (users, books)
users = mydb["users"]
books = mydb["books"]

#CREATE NEW USER (admin)
admin = Users(users, "admin")
admin.password = "password"
admin.save()

#CREATE NEW USER (phil)
phil = Users(users, "phil")
phil.password = "p@s5w0rd"
phil.email = "phil@mongo.com"
phil.save()

#CREATE NEW BOOK (phil)
LotR = Books(books, "Lord of the ring")
LotR.author = "Tolkien"
LotR.description = "One ring to rule them all"
LotR.save()

myclient.close()
