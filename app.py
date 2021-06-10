from flask import Flask

from routes.auth_routes import app_auth
from routes.strategies_routes import app_strategies

app = Flask(__name__)
app.config.from_pyfile('config.py')

app.register_blueprint(app_auth)
app.register_blueprint(app_strategies)


if __name__ == '__main__':
    app.run()