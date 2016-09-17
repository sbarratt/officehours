from flask import render_template, redirect, request, url_for
import config
import json

from app import app, db
from .models import OfficeHour

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    officehours = db.session.query(OfficeHour).all()
    return render_template("index.html", officehours=officehours)

@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    print ("Submit")
    print (request.form)
    class_name = request.form["class"]
    location_name = request.form["location_name"]
    contact = request.form["contact"]
    longitude = float(request.form["longitude"])
    latitude = float(request.form["latitude"])
    print (class_name, location_name, contact, longitude, latitude)
    oh = OfficeHour(
           class_name = class_name,
           location_name = location_name,
           contact = contact,
           longitude = longitude,
           latitude = latitude
    )
    db.session.add(oh)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/markers", methods=["GET"])
def markers():
    officehours = db.session.query(OfficeHour).all()
    ret = []
    for oh in officehours:
        ret.append(oh.asdict())

    return json.dumps(ret)

@app.route("/isalive", methods=["POST"])
def isalive():
    return ""
