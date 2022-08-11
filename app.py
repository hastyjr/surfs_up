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

start off on 9.5.3 :) 