from flask import render_template, redirect, request, url_for
import json
import time
import datetime
import pytz

from app import app, db
from .models import OfficeHour

@app.route("/", methods=["GET"])
def index():
    officehours = db.session.query(OfficeHour).filter(OfficeHour.ended==False).all()
    return render_template("index.html", officehours=officehours)

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    class_name = request.form["class"]
    location_name = request.form["location_name"]
    contact = request.form["contact"]
    longitude = float(request.form["longitude"])
    latitude = float(request.form["latitude"])
    offset = int(request.form["offset"])

    start_time = time.strptime(request.form["start"], '%I:%M %p')
    end_time = time.strptime(request.form["end"], '%I:%M %p')

    start = datetime.datetime.utcnow()
    start = start.replace(hour=start_time.tm_hour, minute=start_time.tm_min) + datetime.timedelta(minutes = offset)

    end = datetime.datetime.utcnow()
    end = end.replace(hour=end_time.tm_hour, minute=end_time.tm_min) + datetime.timedelta(minutes = offset)

    oh = OfficeHour(
           class_name = class_name,
           location_name = location_name,
           contact = contact,
           longitude = longitude,
           latitude = latitude,
           start = start,
           end = end
    )
    db.session.add(oh)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/markers", methods=["GET"])
def markers():
    officehours = db.session.query(OfficeHour).filter(OfficeHour.ended==False).all()
    ret = []
    for oh in officehours:
        ret.append(oh.asdict())

    return json.dumps(ret)

@app.route("/isalive", methods=["POST"])
def isalive():
    return ""
