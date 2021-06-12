from flask import request, Blueprint, jsonify
app_scrapping = Blueprint('app_scrapping',__name__)

from  web_scraping.web_scrapping_main import WebScrappingMain

@app_scrapping.errorhandler(Exception)
def all_exception_handler(error):
    errorMsg = {"message":"Unexpected Error", "body": str(error)}
    return jsonify(errorMsg), 500

@app_scrapping.route('/v1/getStrategies/influencer',methods=["POST"])
def getInfluencerStrategies():
    content = request.json
    strategies = WebScrappingMain()
    return strategies.getSearchedData(content['keyword']), 200