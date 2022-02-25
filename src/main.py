"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import db, Species
from models import db, Vehicles
from models import db, People
from models import db, Starships
from models import db, UserFavoritesSpecies
from models import db, UserFavoritesVehicles
from models import db, UserFavoritesPeople
from models import db, UserFavoritesStarships


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#@app.route('/user', methods=['GET'])
#def handle_hello():

@app.route('/users', methods=['POST'])
def create_user():
    if request.method == 'POST':
        user_name = request.json.get('user_name')
        email = request.json.get('email')   

        user= User()
        user.user_name = user_name
        user.email = email      

        db.session.add(user)
        db.session.commit()     
        
        return jsonify(user.serialize()), 201


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
