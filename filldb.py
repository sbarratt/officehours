from app import db
import datetime
from app.models import OfficeHour

ls = [
    ['PSB 123', 'CS 162', 'stbarratt@gmail.com', 42.4496, -76.4821, datetime.datetime(2016, 9, 17, 14, 30), datetime.datetime(2016, 9, 17, 16, 30)],
]

for l in ls:
    oh = OfficeHour(
        location_name = l[0],
        class_name = l[1],
        contact = l[2],
        latitude = l[3],
        longitude = l[4],
        start = l[5],
        end = l[6]
        )

    db.session.add(oh)
    db.session.commit()