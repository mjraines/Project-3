#import libraries
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask_pymongo import PyMongo

#instance of flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/states_db"

@app.route("/")
def index():
    states_db = mongo.db.states_db.find_one()
    return render_template("index.html", states_db=states_db)

