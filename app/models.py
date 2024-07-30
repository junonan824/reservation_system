from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reservation_date = db.Column(db.Date)
    status = db.Column(db.String(20))
    creator_id = db.Column(db.Integer)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    review_text = db.Column(db.Text)
    rating = db.Column(db.Integer)