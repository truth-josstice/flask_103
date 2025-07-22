from main import db

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    competitions = db.relationship(
        "Competition",
        back_populates="category",
        cascade="all, delete"
    )

