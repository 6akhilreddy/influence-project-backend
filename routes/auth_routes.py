from flask import request, Blueprint, jsonify
app_auth = Blueprint('app_auth',__name__)

from controllers.influencer_controller import InfluencerController
from controllers.brand_controller import BrandController

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
        errorMsg = {"message":"password incorrect", "body": response}
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
        errorMsg = {"message":"password incorrect", "body": response}
        return jsonify(errorMsg), 401