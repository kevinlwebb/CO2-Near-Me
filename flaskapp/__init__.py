from flask import Flask
from joblib import dump, load
from os import path

import os
import json


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

geo_path = os.path.join(basedir, 'data/census.geojson')
with open(geo_path) as f:
    geojson = json.load(f)

machine_path = os.path.join(basedir, 'data/machines.pkl')
if path.exists(machine_path):
    machines = load(machine_path)
else:
    machines = {}
    dump(machines,machine_path)


from flaskapp import routes
