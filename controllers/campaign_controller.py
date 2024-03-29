from models.Campaign import Campaign
from controllers.influencer_controller import InfluencerController
from controllers.brand_controller import BrandController
from factory.validation import Validator

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os
import csv

class CampaignController:
    def __init__(self) -> None:
        self.campaign = Campaign()
        self.validator = Validator()

    def createCampaign(self, campaign):

        # Validator will throw error if invalid
        self.validator.validate(campaign, self.campaign.fields, self.campaign.create_required_fields)
        
        response = self.campaign.create(campaign)

        return response
    
    def deleteCampaign(self, campaignId):

        response = self.campaign.delete(campaignId)

        return response

    def getAllCampaigns(self):

        # get all the campaigns
        campaigns = self.campaign.find({})

        return campaigns
    
    def getCampaignsSpecificToBrand(self, brandusername):

        query = {}
        query['brand_username'] = brandusername

        # get all specific to brand
        brand_campaigns = self.campaign.find(query)

        return brand_campaigns
    
    def getInfluencer(self, influencerUsername):
         # get influencer details
        influencerController = InfluencerController()
        influencer = influencerController.getInfluencer(influencerUsername)

        return influencer
    
    def getBrand(self, brand_username):
        # get brand details
        brandController = BrandController()
        brand = brandController.getBrand(brand_username)

        return brand

    def getListAvg(self, list):
        return sum(list) / len(list)
    
    def getInfluencersSpecificToBrand(self, brandUsername):
        if os.path.isfile('ML/campaign.csv'):
            campaigns = self.getCampaignsSpecificToBrand(brandUsername)

            getAllMinAge = []
            getAllMaxAge = []
            getAllFollowers = []
            getAllPosts = []

            for campaign in campaigns:
                if 'campaign_minage' in campaign:
                    getAllMinAge.append(campaign['campaign_minage'])
                if 'campaign_maxage' in campaign:
                    getAllMaxAge.append(campaign['campaign_maxage'])
                if 'campaign_followers' in campaign:
                    getAllFollowers.append(campaign['campaign_followers'])
                if 'campaign_posts' in campaign:
                    getAllPosts.append(campaign['campaign_posts'])
            
            min_age_avg = self.getListAvg(getAllMinAge)
            max_age_avg = self.getListAvg(getAllMaxAge)
            followers_avg = self.getListAvg(getAllFollowers)
            posts_avg = self.getListAvg(getAllPosts)

            queries = []

            queries.append({'age': { "$lte": max_age_avg }})
            queries.append({'age': { "$gte": min_age_avg }})
            queries.append({'instagram_followers': { "$gte": followers_avg }})
            queries.append({'instagram_posts': { "$gte": posts_avg }})

            influencerController = InfluencerController()
            influencers = influencerController.findInfluencers({'$and':queries})

            for influencer in influencers:
                del influencer['password']

            return influencers
        
        return []

    def getCampaignsSpecificToInfluencer(self, influencerUsername):
        
        influencer = self.getInfluencer(influencerUsername)

        queries = []

        if 'gender' in influencer and 'age' in influencer and 'instagram_followers' in influencer and 'instagram_posts' in influencer:

            queries.append({'campaign_gender': influencer['gender']})
            queries.append({'campaign_minage': { "$lte": influencer['age'] }})
            queries.append({'campaign_maxage': { "$gte": influencer['age'] }})
            queries.append({'campaign_followers': { "$lte": influencer['instagram_followers'] }})
            queries.append({'campaign_posts': { "$lte": influencer['instagram_posts'] }})

            influencer_campaigns = self.campaign.find({'$and':queries})

            return influencer_campaigns
        else:
            return []
    
    def applyToCampaign(self, influencerUsername, campaignId):

        # get campaigns applicable for the influencer
        campaigns_applicable = self.getCampaignsSpecificToInfluencer(influencerUsername)

        if len(campaigns_applicable)>0:

            for campaign in campaigns_applicable:
                if campaign['_id'] == campaignId:
                    del campaign['_id']
                    if 'influencers_applied' in campaign:
                        campaign['influencers_applied'].append(influencerUsername)
                    else:
                        campaign['influencers_applied'] = []
                        campaign['influencers_applied'].append(influencerUsername)
                    
                    self.campaign.update(campaignId, campaign)
                    return True
        
        return False
    
    def getAllApplicationsForCampaign(self, brandUsername):

        # get campagin
        campaigns = self.campaign.find({"brand_username": brandUsername})
        response = []
        for campaign in campaigns:
            resp = {}
            resp["campaign_id"] = campaign["_id"]
            resp["campaign_title"] = campaign["campaign_title"]
            resp["influencers_applied"] = []
            if 'influencers_applied' in campaign:
                for influencer in campaign['influencers_applied']:
                    influencer_data = self.getInfluencer(influencer)
                    influencer_data["application_status"] = self.getApplicationStatus(campaign, influencer_data)
                    resp["influencers_applied"].append(influencer_data)
            response.append(resp)


        return response
    
    def getApplicationStatus(self, campaign, influencer):
        if 'influencers_accepted' in campaign:
            if influencer['username'] in campaign['influencers_accepted']:
                return 'accepted'
        if 'influencers_rejected' in campaign:
            if influencer['username'] in campaign['influencers_rejected']:
                return 'rejected'
        
        return 'pending'


    def acceptApplication(self, campaignId, influencerUsername):
                    
        # get campagin
        campaign = self.campaign.find_by_id(campaignId)

        del campaign['_id']

        if 'influencers_accepted' in campaign:
            campaign['influencers_accepted'].append(influencerUsername)
        else:
            campaign['influencers_accepted'] = []
            campaign['influencers_accepted'].append(influencerUsername)

        return self.campaign.update(campaignId, campaign)

    def rejectApplication(self, campaignId, influencerUsername):
                    
        # get campagin
        campaign = self.campaign.find_by_id(campaignId)

        del campaign['_id']

        if 'influencers_rejected' in campaign:
            campaign['influencers_rejected'].append(influencerUsername)
            print(campaign['influencers_rejected'])
        else:
            campaign['influencers_rejected'] = []
            campaign['influencers_rejected'].append(influencerUsername)
            print(campaign['influencers_rejected'])

        return self.campaign.update(campaignId, campaign)
    
    def getAcceptedApplications(self, campaignId):
        # get campagin
        campaign = self.campaign.find_by_id(campaignId)

        return campaign['influencers_accepted']

    def getRejectedApplications(self, campaignId):
        # get campagin
        campaign = self.campaign.find_by_id(campaignId)

        return campaign['influencers_rejected']
    
    def getApplicationStatusForInfluencer(self, influencerUsername):

        query = {}

        query['influencers_applied'] = {'$in': [influencerUsername] }

        campaigns = self.campaign.find(query)

        response = []
        for campaign in campaigns:
            resp = {}
            resp["campaign_id"] = campaign["_id"]
            resp["campaign_title"] = campaign["campaign_title"]
            influencer_data = self.getInfluencer(influencerUsername)
            resp["application_status"] = self.getApplicationStatus(campaign, influencer_data)
            if 'brand_username' in campaign:
                brand = self.getBrand(campaign["brand_username"])
                print(brand)
                resp["brand_email"] = 'Not Available' if  'email' not in brand else brand['email']
                resp["brand_name"] = 'Not Available' if 'brand_name' not in brand else brand['brand_name']
                resp["brand_headquater"] = 'Not Available' if 'head_quater' not in brand else  brand['head_quater']
            response.append(resp)


        return response
    
    def getAcceptedCampaigns(self, influencerUsername):

        query = {}

        query['influencers_accepted'] = {'$in': [influencerUsername] }

        campaigns = self.campaign.find(query)

        return campaigns
    
    def getRejectedCampaigns(self, influencerUsername):

        query = {}

        query['influencers_rejected'] = {'$in': [influencerUsername] }

        campaigns = self.campaign.find(query)

        return campaigns
    
    def checkCampaignStatus(self, campaignId, influencerUsername):

        # get campagin
        campaign = self.campaign.find_by_id(campaignId)

        if influencerUsername in campaign['influencers_accepted']:
            return 'Accepted'
        elif influencerUsername in campaign['influencers_rejected']:
            return 'Rejected'
        
        return 'Pending'
    
    def generateCSV(self):
        mongo_docs = self.campaign.find({})

        # Convert the mongo docs to a DataFrame
        fieldnames = list(mongo_docs[0].keys())
        fieldnames.remove('_id')

        # compute the output file directory and name
        output_file = os.path.join('ML', 'campaign.csv')
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(mongo_docs)

        return 'generated'

    def trainModel(self):
        # Load the csv file
        df = pd.read_csv("ML/campaign.csv")

        print(df.head())

        # Select independent and dependent variable
        X = df[["campaign_minage", "campaign_maxage", "campaign_followers", "campaign_posts"]]
        y = df["influencer_username"]

        # Split the dataset into train and test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

        # Feature scaling
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test= sc.transform(X_test)

        # Instantiate the model
        classifier = RandomForestClassifier()

        # Fit the model
        classifier.fit(X_train, y_train)

        # Make pickle file of our model
        pickle.dump(classifier, open("ML/model.pkl", "wb"))

        return 'trained'

    def wipeModel(self):
        os.remove("ML/model.pkl")   
        os.remove("ML/campaign.csv")
        return 'wiped' 

    def getBrandSuggestions(self, brandUsername):
        if os.path.isfile('ML/model.pkl'):
            model = pickle.load(open("ML/model.pkl", "rb"))
            return model.predict(brandUsername)
        return []