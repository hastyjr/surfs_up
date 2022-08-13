## Once the Python file is created, let's get our dependencies imported. 
# The first thing we'll need to import is datetime, NumPy, and Pandas. 
# We assign each of these an alias so we can easily reference them later. 
# Add these dependencies to the top of your app.py file.
import datetime as dt
import numpy as np
import pandas as pd

## Add the SQLAlchemy dependencies after the other dependencies you already imported in app.py
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


## add the code to import the dependencies that we need for Flask. 
# You'll import these right after your SQLAlchemy dependencies.
from flask import Flask, jsonify

## set up our database engine for the Flask application
engine = create_engine("sqlite:///hawaii.sqlite")

## reflect the database into our classes.
Base = automap_base()
## reflect the tables
Base.prepare(engine, reflect=True)

## We'll create a variable for each of the classes so that we can reference them late
Measurement = Base.classes.measurement
Station = Base.classes.station

## create a session link from Python to our database 
session = Session(engine)

## Setup Flask to define the Flask app
app = Flask(__name__)

## create and define the welcome route
@app.route("/")
def welcome():
    return (
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

## PRECIATION ROUTE ##
@app.route("/api/v1.0/precipitation")

def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
    ## http://127.0.0.1:5000/api/v1.0/precipitation

## STATIONS ROUTE ##
@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
   ##  http://127.0.0.1:5000/api/v1.0/stations

## TEMPERATURE ROUTE ##
@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
    ## http://127.0.0.1:5000/api/v1.0/tobs

## STATISTICS ROUTE ##
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
    ##  http://127.0.0.1:5000/api/v1.0/temp/2017-06-01/2017-06-30

## START AND END ROUTE #