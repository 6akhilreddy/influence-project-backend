from flask import request, Blueprint, jsonify
app_auth = Blueprint('app_auth',__name__)

from controllers.influencer_controller import InfluencerController
from controllers.brand_controller import BrandController
from controllers.campaign_controller import CampaignController

@app_auth.errorhandler(Exception)
def all_exception_handler(error):
    errorMsg = {"message":"Unexpected Error", "body": str(error)}
    return jsonify(errorMsg), 500

@app_auth.route('/v1/signup/influencer',methods=["POST"])
def influencerSignup():
    content = request.json
    influencerController = InfluencerController()
    response = influencerController.createInfluencer(content)
    successMsg = {"message":"Successfully Created Influencer", "body": response}
    return jsonify(successMsg), 201

@app_auth.route('/v1/signin/influencer',methods=["POST"])
def influencerSignin():
    content = request.json
    influencerController = InfluencerController()
    response = influencerController.verifyInfluencer(content)
    if response:
        successMsg = {"message":"Successfully Verified Influencer", "body": response}
        return jsonify(successMsg), 201
    else:
        errorMsg = {"message":"password incorrect", "body": "password incorrect"}
        return jsonify(errorMsg), 401

@app_auth.route('/v1/signup/brand',methods=["POST"])
def brandSignup():
    content = request.json
    brandController = BrandController()
    response = brandController.createBrand(content)
    successMsg = {"message":"Successfully Created Influencer", "body": response}
    return jsonify(successMsg), 201

@app_auth.route('/v1/signin/brand',methods=["POST"])
def brandSignin():
    content = request.json
    brandController = BrandController()
    response = brandController.verifyBrand(content)
    if response:
        successMsg = {"message":"Successfully Verified Influencer", "body": response}
        return jsonify(successMsg), 201
    else:
        errorMsg = {"message":"password incorrect", "body": "password incorrect"}
        return jsonify(errorMsg), 401

@app_auth.route('/v1/influencer/profile/<username>',methods=["GET"])
def getInfluencerProfile(username):
    print(username)
    influencerController = InfluencerController()
    response = influencerController.getInfluencer(username)
    successMsg = {"message":"Successfully Returned Influencer", "body": response}
    return jsonify(successMsg), 200

@app_auth.route('/v1/influencer/profile/update',methods=["PUT"])
def updateInfluencerProfile():
    content = request.json
    influencerController = InfluencerController()
    response = influencerController.updateInfluencer(content)
    successMsg = {"message":"Successfully Updated Influencer", "body": response}
    return jsonify(successMsg), 200

@app_auth.route('/v1/brand/profile/<username>',methods=["GET"])
def getBrandProfile(username):
    print(username)
    brandController = BrandController()
    response = brandController.getBrand(username)
    successMsg = {"message":"Successfully Returned Brand", "body": response}
    return jsonify(successMsg), 200

@app_auth.route('/v1/brand/profile/update',methods=["PUT"])
def updateBrandProfile():
    content = request.json
    brandController = BrandController()
    response = brandController.updateBrand(content)
    successMsg = {"message":"Successfully Updated Brand", "body": response}
    return jsonify(successMsg), 200

@app_auth.route('/v1/brand/campaign/create',methods=["POST"])
def createCampaign():
    content = request.json
    campaignController = CampaignController()
    response = campaignController.createCampaign(content)
    successMsg = {"message":"Successfully Created campaign", "body": response}
    return jsonify(successMsg), 201

@app_auth.route('/v1/brand/campaign/<brandUsername>',methods=["GET"])
def getCampaign(brandUsername):
    campaignController = CampaignController()
    response = campaignController.getCampaignsSpecificToBrand(brandUsername)
    successMsg = {"message":"Successfully Returned Campaign", "body": response}
    return jsonify(successMsg), 200

@app_auth.route('/v1/influencer/campaigns',methods=["GET"])
def getAllCampaigns():
    campaignController = CampaignController()
    response = campaignController.getAllCampaigns()
    successMsg = {"message":"Successfully Returned Campaigns", "body": response}
    return jsonify(successMsg), 200

@app_auth.route('/v1/influencer/campaigns/filtered/<influencerUsername>',methods=["GET"])
def getFilteredCampaigns(influencerUsername):
    campaignController = CampaignController()
    response = campaignController.getCampaignsSpecificToInfluencer(influencerUsername)
    successMsg = {"message":"Successfully Returned Campaigns", "body": response}
    return jsonify(successMsg), 200

@app_auth.route('/v1/influencer/campaign/apply',methods=["POST"])
def applyCampaign():
    content = request.json
    campaignController = CampaignController()
    response = campaignController.applyToCampaign(content['username'], content['campaignId'])
    if response:
        successMsg = {"message":"Successfully Applied campaign", "body": response}
        return jsonify(successMsg), 201
    else:
        errorMsg = {"message":"Not Applicable", "body": "No applicable"}
        return jsonify(errorMsg), 401

@app_auth.route('/v1/brand/campaign/applications/<brandUsername>',methods=["GET"])
def getApplications(brandUsername):
    campaignController = CampaignController()
    response = campaignController.getAllApplicationsForCampaign(brandUsername)
    successMsg = {"message":"Successfully Returned Campaign", "body": response}
    return jsonify(successMsg), 200

@app_auth.route('/v1/brand/campaign/application/accept',methods=["POST"])
def acceptApplication():
    content = request.json
    campaignController = CampaignController()
    response = campaignController.acceptApplication(content['campaignId'], content['influencerUsername'])
    successMsg = {"message":"Successfully Returned Campaign", "body": response}
    return jsonify(successMsg), 200

@app_auth.route('/v1/brand/campaign/application/reject',methods=["POST"])
def rejectApplication():
    content = request.json
    campaignController = CampaignController()
    response = campaignController.rejectApplication(content['campaignId'], content['influencerUsername'])
    successMsg = {"message":"Successfully Returned Campaign", "body": response}
    return jsonify(successMsg), 200


@app_auth.route('/v1/influencer/application/status/<influencerUsername>',methods=["GET"])
def getAllApplicationStatus(influencerUsername):
    campaignController = CampaignController()
    response = campaignController.getApplicationStatusForInfluencer(influencerUsername)
    successMsg = {"message":"Successfully Returned Campaign", "body": response}
    return jsonify(successMsg), 200

@app_auth.route('/v1/brand/campaign/<campaignId>', methods=["DELETE"])
def deleteCampaign(campaignId):
    campaignController = CampaignController()
    response = campaignController.deleteCampaign(campaignId)
    successMsg = {"message":"Successfully Deleted Campaign", "body": response}
    return jsonify(successMsg), 200


    