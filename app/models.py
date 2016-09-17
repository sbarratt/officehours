from app import db

class OfficeHour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(120))
    class_name = db.Column(db.String(120), index=True)
    contact = db.Column(db.String(120), index=True)
    latitude = db.Column(db.Float, index=True)
    longitude = db.Column(db.Float, index=True)
    start = db.Column(db.DateTime, index=True)
    end = db.Column(db.DateTime, index=True)

    def asdict(self):
        return {
                'location_name': self.location_name,
                'class_name': self.class_name,
                'contact': self.contact,
                'latitude': self.latitude,
                'longitude': self.longitude,
                'start': self.start.isoformat(),
                'end': self.end.isoformat()
        }
