from main import db

class Competition(db.Model):
    __tablename__ = "competitions"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    prize = db.Column(db.String())
    year = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"),nullable=False)
    category = db.relationship(
        "Category",
        back_populates="competitions"
    )