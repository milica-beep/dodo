from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes.auth import auth
from routes.task import task

import db_con

app = Flask(__name__)
CORS(app)
app.debug = True

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

if __name__ == "__main__":
    app.register_blueprint(auth)
    app.register_blueprint(task)

    app.run()

