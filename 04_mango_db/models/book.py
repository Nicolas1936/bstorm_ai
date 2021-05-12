import pymongo

class Books:
    def save(self):
        if not self._id:
            self.collection.insert_one({ "title": self.title, "description": self.description, "author": self.author })
            book = self.collection.find_one({"title" : self.title})
            self._id = book["_id"]
        else:
            self.collection.update_one({ "title": self.title }, { "$set": { "username": self.title, "description": self.description, "author": self.author }})
    
    def delete(self):
        if self._id:
            self.collection.find_one_and_delete({ "title": self.title })

    def __init__(self, collection, title):
        self.collection = collection
        user = self.collection.find_one({ "title": title })
        if user:
            print(user)
            self._id = user["_id"]
            self.title = user["title"]
            self.description = user["description"]
            self.author = user["author"]
        else:
            self._id = 0
            self.title = title
            self.description = ""
            self.author = ""