
from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather_queries = db.relationship('Weather', backref='queried_by', lazy=True)
    saved_locations = db.relationship('Location', backref='saved_by', lazy=True)

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String(20), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    condition = db.Column(db.String(100), nullable=False)
    queried_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    saved_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    __table_args__ = (db.UniqueConstraint('longitude', 'latitude'),)
