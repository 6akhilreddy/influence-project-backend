from flask import request, Blueprint, jsonify
app_strategies = Blueprint('app_strategies',__name__)

from  web_scraping.web_scrapping_main import WebScrappingMain

@app_strategies.errorhandler(Exception)
def all_exception_handler(error):
    errorMsg = {"message":"Unexpected Error", "body": str(error)}
    return jsonify(errorMsg), 500

@app_strategies.route('/v1/getStrategies/influencer',methods=["POST"])
def getInfluencerStrategies():
    content = request.json
    strategies = WebScrappingMain()
    return strategies.getSearchedData(content['keyword']), 200