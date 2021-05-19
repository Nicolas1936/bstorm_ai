import pymongo
from pymongo.message import query
from bson.json_util import dumps

#CONNECT TO THE DATABASE
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

dblist = myclient.list_database_names()
print(dblist)
#CREATE A NEW DATABASE
mydb = myclient["mydb"]

if "mydb" in dblist:
    print("database already exist!")
else:
    print("create a new database")

print(dblist)

#CREATE A NEW COLLECTION users
users = mydb['users']
users.drop()

#INSERT SOME DATA IN THE COLLECTION users
data = [    {   'lastname'  :   'Blanchard', 
                'firstname' :   'Nicolas'
            },
            {
                'lastname'  :   'Vlamynck',
                'firstname' :   'Kathleen'
            }
]
users.insert_many(data)

#INSERT ONE DATA IN THE COLLECTION users
one_data = {
    'lastname'  :   'Perret',
    'firstname' :   'Pierre'
}
users.insert_one(one_data)

#GET ALL THE DATA FROM THE COLLECTION
[print(user) for user in users.find()]
print()
#GET ONE DATA FROM THE COLLECTION
print(users.find_one(filter={'firstname' : 'Kathleen'}))
print()
#OR
[print(user) for user in users.find(projection={'_id' : 0, 'firstname' : 1})]

#UPDATE ONE DATA IN THE COLLECTION
users.update_one(
    {'lastname'     :   'Blanchard'},
    {'$set'  :   {'firstname'    :   'Nico'}}
)

#DELETE ONE DATA IN THE COLLECTION

for user in users.find():
    print(user)

kp_cursor = users.find({'$or' : [{'firstname' : 'Kathleen'}, { 'lastname' : 'Perret'}]})

print(dumps(kp_cursor, indent=4))

