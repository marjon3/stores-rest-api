from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

# virtual environment instructions:

# Create a new virtual environment: python -m virtualenv venv
# Activate: venv\Scripts\activate

# Install Flask: (if needed): pip install Flask
# Install JWT: pip install Flask-JWT
# Install Flask-RESTFUL: (if needed): pip install Flask-RESTful
# Install JWT: pip install Flask-JWT
# Install FLASK-SQLAlchemy: pip install Flask-SQLAlchemy

# Version of Python: python --version
# Show installed packages: pip freeze
# Deactivate: deactivate

# Run program

# Not inside folder: python code/app.py
# Inside folder: python app.py

# remove file for database: rm data.db

# Database instructions: