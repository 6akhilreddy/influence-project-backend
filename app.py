from flask import Flask, request
from  web_scraping.web_scrapping_main import WebScrappingMain

from routes.auth_routes import app_auth
from routes.strategies_routes import app_strategies

app = Flask(__name__)
app.config.from_pyfile('config.py')

app.register_blueprint(app_auth)
app.register_blueprint(app_strategies)

@app.route('/getStrategies',methods=["POST"])
def getStrategies():
    content = request.json
    strategies = WebScrappingMain()
    return strategies.getSearchedData(content['keyword'])

if __name__ == '__main__':
    app.run()