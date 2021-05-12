class Users:
    def save(self):
        if not self._id:
            self.collection.insert_one({ "username": self.username, "password": self.password, "email": self.email })
            user = self.collection.find_on({"username" : self.username})
            self._id = user["_id"]
        else:
            self.collection.update_one({ "username": self.username }, { "$set": { "username": self.username, "password": self.password, "email": self.email }})
    
    def delete(self):
        if self._id:
            self.collection.find_one_and_delete({ "username": self.username })

    def __init__(self, collection, username):
        self.collection = collection
        user = self.collection.find_one({ "username": username })
        if user:
            print(user)
            self._id = user["_id"]
            self.username = user["username"]
            self.password = user["password"]
            self.email = user["email"]
        else:
            self._id = 0
            self.username = username
            self.password = ""
            self.email = ""