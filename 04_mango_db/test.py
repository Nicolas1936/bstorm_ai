from enum import unique
import pymongo

#CONNECT TO THE DATABASE
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#GET ALL THE DATABASE
dblist = myclient.list_database_names()

#SEE ALL THE DATABASE
for db in dblist:
    print(db)

#CREATE OR GET THE DATABASE "Example_IA"
mydb = myclient["Example_IA"]
if "Example_IA" in dblist:
    print("database already exist!")

print("Initalize data...")

#CREATE OR GET THE COLLECTION "users"
users = mydb["users"]

users.create_index([("username", pymongo.ASCENDING)], unique=True)

#CREATE THE COLLOCTION "users" IF EMPTY
if users.count_documents({}) == 0:
    default_users = [
        { "username": "admin", "password": "admin", "email": "admin@admin.com" },
        { "username": "test", "password": "admin", "email": "test@admin.com" },
        { "username": "qwerty", "password": "admin", "email": "qwerty@admin.com" },
        { "username": "qwe", "password": "admin", "email": "qwe@admin.com" },
        { "username": "asd", "password": "admin", "email": "asd@admin.com" }
    ]
    users.insert_many(default_users)
else:
    print("users exist")

#SELECT ALL FIELDS FROM COLLECTION "users"
#SELECT * FROM users
for user in users.find():
    print(user)

#SELECT ALL FIELDS, DO NOT DISPLAY _ID
#SELECT username, email FROM user
for user in users.find({}, {"_id": 0, "username": 1, "email":1 }).sort("username", -1):
    print(user)

#Update a field
#UPDATE THE PASSWORD OF THE USER 'test'
#UPDATE users SET password='newpassword' WHERE username='test'
query = {"username" : "test"}
new_val = {"$set" : {"password" : "newpassword"}}
users.update_one(query, new_val)
print(users.find_one(query))

#DELETE THE FIELDS WHERE THE USER IS 'asd'
#DELETE FROM users WHERE username='asd';
users.find_one_and_delete({"username" : "asd"})
for user in users.find({}, {"_id": 0, "username": 1, "email":1 }).sort("username"):
    print(user)


#Book : Title Description author

#Insertion de la table Book
books = mydb["books"]
books.drop()
books.create_index([("title", pymongo.ASCENDING)], unique=True)


if books.count_documents({}) == 0:
    default_books = [
        {"title" : "the Alchimiste", "description" : "a shepherd's journey", "author" : "Paolo Cueno"},
        {"title" : "les miserables", "description" : "...", "author" : "Victor Hugo"},
        {"title" : "t3", "description" : "a shepherd's journey", "author" : "Camus"},
        {"title" : "t4", "description" : "a shepherd's journey", "author" : "Franz Weber"}
    ]

    books.insert_many(default_books)
else:
    print("books exist")

books.insert_one({"title" : "t5", "description" : "blabla", "author" : "Jean"})

for book in books.find({}):
    print(book)

#WHERE
print("WHERE TITLE = T5")
for book in books.find({"title" : "t5"}, {"_id": 0}):
    print(book)

#UPDATE
print("UPDATE")
books.update_one({"title" : "t3"}, {"$set" : {"title" : "t33"}})
for book in books.find({}):
    print(book)

#DELETE
print("DELETE")
books.delete_one({"title" : "t4"})
for book in books.find({}):
    print(book)




