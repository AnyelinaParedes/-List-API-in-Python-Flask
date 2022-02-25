from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password":self.password,
            "is_active":self.is_active,
            
        }
class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    clasificaction= db.Column(db.String(250))
    language = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "clasificaction": self.clasificaction,
            "language_period": self.language,
            "eye_color": self.eye_color,
           
        }

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    model= db.Column(db.String(250))
    passenger = db.Column(db.String(250), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "passenger": self.passenger,
        }
    
class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    height= db.Column(db.String(250))
    skin_color = db.Column(db.String(250), nullable=False)
    gender= db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "skin_color": self.skin_color,
            "genger": self.genger,
        }
    
class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(250))
    cargo_capacity= db.Column(db.String(250))
    hyperdrive_rating = db.Column(db.String(250), nullable=False)
    manufacturer= db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "model": self.model,
            "cargo_capacity": self.cargo_capacity,
            "hyperdrive_rating": self.hyperdrive_rating,
            "manufacture": self.manufacture,
        }
    
class UserFavoritesSpecies(db.Model):
    __tablename__ = 'userFavoritesSpecies'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    species = db.relationship('Species')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user": self.user,
            "species_id": self.species_id,
            "species": self.species,
        }


class UserFavoritesVehicles(db.Model):
    __tablename__ = 'userFavoritesVehicles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    vehicles = db.relationship('Vehicles')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user": self.user,
            "vehicles_id": self.vehicles_id,
            "vehicles": self.vehicles,
        }

class UserFavoritesPeople(db.Model):
    __tablename__ = 'userFavoritesPeople'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    people = db.relationship('People')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user": self.user,
            "people_id": self.people_id,
            "people": self.people,
        }

class UserFavoritesStarships(db.Model):
    __tablename__ = 'userFavoritesStarships'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    starships_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starships = db.relationship('Starships')  

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user": self.user,
            "starships_id": self.starships_id,
            "starships": self.starships,
        }  