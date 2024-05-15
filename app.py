from flask import Flask
# For Configuration
from flask_smorest import Api
# For Blueprint Registration
# from flask_smorest.blueprint import Blueprint 
# database
from db import db

import os

# Flask Login Manager
from flask_login import LoginManager
# Models
from models import userModel

app = Flask(__name__)

'''
------------------------Login Manager For Flask-----------------------
'''

login_manager = LoginManager()
# Initializing login manager
login_manager.init_app(app)

# User Loader
@login_manager.user_loader
def load_user(id):
    return userModel.query.get(id)
'''
-------------------EOL-----Login Manager For Flask -----------------------
'''

'''
-----------------------Registration of Blueprints Below-----------------------
'''
from blps.signup import blp as blpSignup
app.register_blueprint(blpSignup)

from blps.login import blp as blpLogin
app.register_blueprint(blpLogin)
'''
-----------------------Registration of Blueprints Done-----------------------
'''



'''
-----------------------Flask smorest configuration start-----------------------
'''
# Secret key
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
# sqlite configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
api = Api(app)
'''
-----------------------Flask smorest configuration Done-----------------------
'''




# Initializing database
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(debug=True)

