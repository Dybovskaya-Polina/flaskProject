from app import db


class Doctors(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Strng(50), unique=True)
    users = db.relationship()
