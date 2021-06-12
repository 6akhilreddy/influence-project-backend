from factory.database import Database
from utilities.constants import influencer_collection_name


class Influencer(object):
    def __init__(self):
        self.db = Database()

        self.collection_name = influencer_collection_name  # collection name

        self.fields = {
            "username": "string",
            "email": "string",
            "password": "string",
            "name":"string",
            "gender":"string",
            "description":"string",
            "instagram_handle": "string",
            "age": "int",
            "instagram_posts":"int",
            "instagram_followers":"int",
            "facebook_handle":"string",
            "twitter_handle":"string",
            "contact": "string",
            "interests": list,
            "brands": list,
            "created": "datetime",
            "updated": "datetime"
        }

        # Fields required for CREATE
        self.create_required_fields = ["username", "email", "password"]

        # Fields required for UPDATE
        self.update_required_fields = ["username"]

        # Fields required for Login
        self.login_required_fields = ["username", "password"]
    
    # To test if the the object gets automatically destory after the api call
    # def __del__(self):
    #     print("I'm being automatically destroyed. Goodbye!")

    def create(self, user):
        res = self.db.insert(user, self.collection_name)
        return res

    def find(self, query):  # find all
        return self.db.find(query, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, user):
        return self.db.update(id, user,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)