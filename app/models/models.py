from extensions import db

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    medications = db.relationship("Medication", back_populates="children")

class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    dose = db.Column(db.String(200))
    frequency = db.Column(db.Integer)
    child_id = db.Column(db.ForeignKey("child.id"))
    # Not sure about adding a Bool column for given/not given. Maybe address on frontend?

    children = db.relationship("Child", back_populates="medications")