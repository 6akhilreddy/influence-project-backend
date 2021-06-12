from factory.database import Database
from utilities.constants import campaigns_collection_name


class Campaign(object):
    def __init__(self):
        self.db = Database()

        self.collection_name = campaigns_collection_name  # collection name

        self.fields = {
            "campaign_title":"string",
            "campaign_details": "string",
            "brand_username": "string",
            "campaign_minage":"int",
            "campaign_maxage": "int",
            "campaign_followers": "int",
            "campaign_posts": "int",
            "campaign_gender": "string",
            "campaign_interests":list,
            "influencers_applied": list,
            "influencers_accepted":list,
            "influencers_rejected":list,
            "created": "datetime",
            "updated": "datetime"
        }

        # Fields required for CREATE
        self.create_required_fields = ["campaign_title", "campaign_details", "brand_username"]

        # Fields required for UPDATE
        self.update_required_fields = ["brand_id"]

    def create(self, campaign):
        res = self.db.insert(campaign, self.collection_name)
        return res

    def find(self, campaign):  # find all
        return self.db.find(campaign, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, campaign):
        return self.db.update(id, campaign,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)