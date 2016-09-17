from app import db
from app.models import OfficeHour

for oh in db.session.query(OfficeHour).all():
    print oh.asdict()
