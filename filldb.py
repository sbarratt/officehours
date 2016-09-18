from app import db
import datetime
from app.models import OfficeHour
import random

ls = [
    ['Duffield Auditorium', 'CS 2110', 'java@cornell.edu', 42.444796, -76.482557, datetime.datetime.utcnow(), datetime.datetime.utcnow() + datetime.timedelta(hours=random.randint(1,3))],
    ['Duffield Alcove', 'CS 1110', 'python@cornell.edu', 42.444973, -76.482264, datetime.datetime.utcnow(), datetime.datetime.utcnow() + datetime.timedelta(hours=random.randint(1,3))],
    ['Statler Library', 'HADM 4300', 'wines@cornell.edu', 42.445493, -76.481999, datetime.datetime.utcnow(), datetime.datetime.utcnow() + datetime.timedelta(hours=random.randint(1,3))],
    ['Olin Library', 'PSCH 1100', 'psych@cornell.edu', 42.447672, -76.484555, datetime.datetime.utcnow(), datetime.datetime.utcnow() + datetime.timedelta(hours=random.randint(1,3))],
    ['Dairy Bar', 'NS 4200', 'food@cornell.edu', 42.447150, -76.470248, datetime.datetime.utcnow(), datetime.datetime.utcnow() + datetime.timedelta(hours=random.randint(1,3))],
    ['Uris Library', 'MAE 3210', 'waves@cornell.edu', 42.447759, -76.485075, datetime.datetime.utcnow(), datetime.datetime.utcnow() + datetime.timedelta(hours=random.randint(1,3))],
    ['Kennedy Hall', 'INFO 4240', 'green@cornell.edu', 42.447989, -76.479131, datetime.datetime.utcnow(), datetime.datetime.utcnow() + datetime.timedelta(hours=random.randint(1,3))],
    ['Mann Library', 'ECE 4320', 'circuits@cornell.edu', 42.448632, -76.476523, datetime.datetime.utcnow(), datetime.datetime.utcnow() + datetime.timedelta(hours=random.randint(1,3))],
    ['Upson Hall', 'MAE 3240', 'mech@cornell.edu', 42.443834, -76.482037, datetime.datetime.utcnow(), datetime.datetime.utcnow() + datetime.timedelta(hours=random.randint(1,3))]
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
