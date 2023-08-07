from ..extensions import db

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    medications = db.relationship("Medication", back_populates="children")
