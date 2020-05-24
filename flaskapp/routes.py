from flaskapp import app
from flask import render_template, request
from flaskapp import machines, machine_path
from joblib import dump

import geopandas as gpd
import pandas as pd
import geocoder


myloc = geocoder.ip('me')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/geo')
def geo():

    return geojson

@app.route('/current')
def current():
    current = gpd.GeoDataFrame(geometry=gpd.points_from_xy([myloc.latlng[1]],[myloc.latlng[0]]))
    current['geometry'] = current.geometry.buffer(0.02)

    df = pd.DataFrame(machines).T
    df.lon = df.lon.astype('float')
    df.lat = df.lat.astype('float')
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon,df.lat))

    print(gdf.to_json())

    return gdf.to_json()

@app.route('/receive', methods=['POST'])
def receive():
    lon = request.form["lon"]
    lat = request.form["lat"]
    name = request.form["name"]
    co2 = request.form["value"]

    if name in machines:
        machines[name]["all"].append(co2)
        machines[name]["current"] = co2
    else:
        machines[name] = {"all": [co2],"lon": lon, "lat": lat, "current": co2}
    
    dump(machines,machine_path)
    
    return "SUCCESS"

@app.route('/data')
def data():

    return machines