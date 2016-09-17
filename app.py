from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)

from .models import OfficeHour

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    class_name = request.args.get("class")
    location_name = request.args.get("location_name")
    contact = request.args.get("contact")
    longitude = request.args.get("longitude")
    latitude = request.args.get("latitude")
    oh = OfficeHour(
           class_name = class_name,
           location_name = location_name,
           contact = contact,
           longitude = longitude,
           latitude = latitude
    )
    db.session.add(oh)
    db.session.commit()
    redirect("hello")


@app.route("/isalive")
def hello():
    return

app.run(debug=True)
