import unittest
import requests
import json

base_url = 'http://localhost:5000/'

class InfluencerLoginUnitTestCase(unittest.TestCase):

    login_data = requests.post(base_url+'/v1/signin/influencer', json={"username": "akshay", "password":"akshay123"})

    # check response is 200
    def test_index(self):
        status_code = self.login_data.status_code
        self.assertEqual(status_code, 201)
    
    # check if data return is correct
    def test_index_content(self):
        content = json.loads(self.login_data.content.decode("utf-8"))["message"]
        self.assertEqual(content, 'Successfully Verified Influencer')

class BrandLoginUnitTestCase(unittest.TestCase):

    login_data = requests.post(base_url+'/v1/signin/brand', json={"username": "apple", "password":"apple123"})

    # check response is 200
    def test_index(self):
        status_code = self.login_data.status_code
        self.assertEqual(status_code, 201)
    
    # check if data return is correct
    def test_index_content(self):
        content = json.loads(self.login_data.content.decode("utf-8"))["message"]
        self.assertEqual(content, 'Successfully Verified Influencer')

class InfluencerProfileUnittestCase(unittest.TestCase):

    profile_data = requests.get(base_url+'/v1/influencer/profile/akshay')

    # check response is 200
    def test_index(self):
        status_code = self.profile_data.status_code
        self.assertEqual(status_code, 200)
    
    # check if data return is correct
    def test_index_content(self):
        content = json.loads(self.profile_data.content.decode("utf-8"))["message"]
        self.assertEqual(content, 'Successfully Returned Influencer')

class BrandProfileUnittestCase(unittest.TestCase):

    profile_data = requests.get(base_url+'/v1/brand/profile/apple')

    # check response is 200
    def test_index(self):
        status_code = self.profile_data.status_code
        self.assertEqual(status_code, 200)
    
    # check if data return is correct
    def test_index_content(self):
        content = json.loads(self.profile_data.content.decode("utf-8"))["message"]
        self.assertEqual(content, 'Successfully Returned Brand')

class BrandcampaignsUnittestCase(unittest.TestCase):

    campaign_data = requests.get(base_url+'/v1/brand/campaign/apple')

    # check response is 200
    def test_index(self):
        status_code = self.campaign_data.status_code
        self.assertEqual(status_code, 200)
    
    # check if data return is correct
    def test_index_content(self):
        content = json.loads(self.campaign_data.content.decode("utf-8"))["message"]
        self.assertEqual(content, 'Successfully Returned Campaign')

class InfluencercampaignsUnittestCase(unittest.TestCase):

    campaign_data = requests.get(base_url+'/v1/influencer/campaigns')

    # check response is 200
    def test_index(self):
        status_code = self.campaign_data.status_code
        self.assertEqual(status_code, 200)
    
    # check if data return is correct
    def test_index_content(self):
        content = json.loads(self.campaign_data.content.decode("utf-8"))["message"]
        self.assertEqual(content, 'Successfully Returned Campaigns')

class InfluencerFilteredcampaignsUnittestCase(unittest.TestCase):

    campaign_data = requests.get(base_url+'/v1/influencer/campaigns/filtered/akshay')

    # check response is 200
    def test_index(self):
        status_code = self.campaign_data.status_code
        self.assertEqual(status_code, 200)
    
    # check if data return is correct
    def test_index_content(self):
        content = json.loads(self.campaign_data.content.decode("utf-8"))["message"]
        self.assertEqual(content, 'Successfully Returned Campaigns')

class BrandApplicationsUnittestCase(unittest.TestCase):
    application_data = requests.get(base_url+'/v1/brand/campaign/applications/apple')
    # check response is 200
    def test_index(self):
        status_code = self.application_data.status_code
        self.assertEqual(status_code, 200)
    
    # check if data return is correct
    def test_index_content(self):
        content = json.loads(self.application_data.content.decode("utf-8"))["message"]
        self.assertEqual(content, 'Successfully Returned Campaign')

if __name__ == "__main__":
    unittest.main()