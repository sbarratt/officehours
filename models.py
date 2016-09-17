from app import db

class OfficeHour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(120))
    class_name = db.Column(db.String(120), index=True)
    user = db.Column(db.String(120), index=True)
    latitude = db.Column(db.Float, index=True)
    longitude = db.Column(db.Float, index=True)
