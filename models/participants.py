from main import db

class Participant(db.Model):
    __tablename__ = "participants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)