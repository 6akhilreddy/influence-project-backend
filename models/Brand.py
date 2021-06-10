from factory.database import Database
from utilities.constants import brands_collection_name


class Brand(object):
    def __init__(self):
        self.db = Database()

        self.collection_name = brands_collection_name  # collection name

        self.fields = {
            "username": "string",
            "password": "string",
            "email":"string",
            "brand_name": "string",
            "industry": "string",
            "contact": "string",
            "influencers": list,
            "created": "datetime",
            "updated": "datetime"
        }

        # Fields required for CREATE
        self.create_required_fields = ["username", "password", "email", "brand_name"]

        # Fields required for UPDATE
        self.update_required_fields = ["username","password"]

        # Fields required for Login
        self.login_required_fields = ["username","password"]

    def create(self, company):
        res = self.db.insert(company, self.collection_name)
        return res

    def find(self, company):  # find all
        return self.db.find(company, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, company):
        return self.db.update(id, company,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)