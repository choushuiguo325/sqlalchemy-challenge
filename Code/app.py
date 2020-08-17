# step 2 - climate analysis

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,inspect,func

from flask import Flask,jsonify
import pandas as pd

# access the sqlite file: 
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
measurements = Base.classes.measurement
session = Session(bind = engine)

def calc_temps(start,end):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(measurements.tobs), func.avg(measurements.tobs), func.max(measurements.tobs)).\
        filter(measurements.date >= start).filter(measurements.date <= end).all()


def calc_temps_start(start):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(measurements.tobs), func.avg(measurements.tobs), func.max(measurements.tobs)).\
        filter(measurements.date >= start).all()



routes = {
    "1":"Query Precipitation Data from '2016-08-03' to '2017-08-03' : /api/v1.0/precipitation",
    "2":"Query Station Data: /api/v1.0/stations",
    "3":"Query Temperature Data: /api/v1.0/tobs",
    "4":"Query Temperature Description for A Given Start: /api/v1.0/<start>",
    "5":"Query Temperature Description for A Given Start-end Range: /api/v1.0/<start>/<end>",
}


precipitations_dict = pd.read_csv("../Output/precipitations.csv").set_index("Date").to_dict()["Precipitation Scores"]
stations_dict = pd.read_csv("../Resources/hawaii_stations.csv").to_dict(orient='records')
active_temp_dic = pd.read_csv("../Output/tem_active_station.csv").set_index("Date").to_dict()["Temperature"]


app = Flask("__name__")


@app.route("/")
def home_page():
    return jsonify(routes)
     
        
@app.route("/api/v1.0/precipitation")
def precipitation():
        
    return jsonify(precipitations_dict)
    

        
@app.route("/api/v1.0/stations")
def stations():
                
    return jsonify(stations_dict)
    
    
@app.route("/api/v1.0/tobs")
def tobs():
                
    return jsonify(active_temp_dic)

@app.route("/api/v1.0/<start>")
def temp_start(start):
    results = calc_temps_start(start)[0]
    return (
        f"Minimum temperature: {results[0]};"
        f"Average temperature: {round(results[1],1)};"
        f"Maximum temperature: {results[2]};"
    )

@app.route("/api/v1.0/<start>/<end>")
def temp_range(start,end):
    results = calc_temps(start,end)[0]
    return (
        f"Minimum temperature: {results[0]};"
        f"Average temperature: {round(results[1],1)};"
        f"Maximum temperature: {results[2]};"
    )
    
if __name__ == "__main__":
    app.run(debug=True)