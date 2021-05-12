import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db_list = myclient.list_database_names()

print(db_list)
