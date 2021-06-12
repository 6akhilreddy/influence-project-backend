from flask import Flask
from flask_cors import CORS
from routes.auth_routes import app_auth
from routes.scrapping_routes import app_scrapping

app = Flask(__name__)
app.config.from_pyfile('config.py')

CORS(app)

app.register_blueprint(app_auth)
app.register_blueprint(app_scrapping)


if __name__ == '__main__':
    app.run()