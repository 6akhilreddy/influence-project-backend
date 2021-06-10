from flask import request, Blueprint, jsonify
app_strategies = Blueprint('app_strategies',__name__)

@app_strategies.errorhandler(Exception)
def all_exception_handler(error):
    errorMsg = {"message":"Unexpected Error", "body": str(error)}
    return jsonify(errorMsg), 500

