
from models.user import Users
from models.book import Books
from models.editor import Editor

import pymongo



myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# get database 
dblist = myclient.list_database_names()

for db in dblist:
    print(db)

mydb = myclient["Example_IA"]
if "Example_IA" in dblist:
    print("database already exist!")

print("initialize data...")

users = mydb["users"]
books = mydb["books"]

admin = Users(users, "admin")
admin.password = "password"
admin.save()

phil = Users(users, "phil")
phil.password = "p@s5w0rd"
phil.email = "phil@mongo.com"
phil.save()

LotR = Books(books, "Lord of the ring")
LotR.author = "Tolkien"
LotR.description = "One ring to rule them all"
LotR.save()

myclient.close()