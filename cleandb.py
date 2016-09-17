from app import db
from app.models import OfficeHour
import datetime

for oh in db.session.query(OfficeHour).filter(OfficeHour.ended == False).all():
    if oh.end < datetime.datetime.now():
        oh.ended = True

db.session.commit()
