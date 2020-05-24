# CO<sub>2</sub> Near Me
*CO<sub>2</sub> Map and API*

## Overview
**CO<sub>2</sub> Near Me** is a web application that has a map with an accompanying API that utilizes collected CO<sub>2</sub> data from devices all over the world. Embedded Devices can send data to the provided endpoint, and the map will display the location alongside the CO<sub>2</sub> value. As the the application is built out, the API will be able to take in longitude and latitude values and give back specific values for the area.

## Website
https://co2nearme.herokuapp.com/
- Deleted

## DEVPOST
https://devpost.com/software/co2-near-me

## File Layout

    .
    ├── flaskapp
    │   ├── __init__.py                      # Flask file that runs app
    │   ├── routes.py                        # Flask file that contains endpoints
    │   ├── data
    │   │   └── machines.pkl                 # Pickle file of devices dictionary 
    │   ├── templates   
    │   │   └── index.html                   # Map page of web app
    │   └── static   
    |
    ├── helper
    │   ├── raspsetup                        # Script that installs needed libraries  
    │   └── report.py                        # Python script that sends data from device
    ├── Procfile                             # Specifies commands executed on startup
    ├── run.py                               # Entry point for the application
    └── requirements.txt                     # List of libraries to be installed


## Terms
- **eCO<sub>2</sub>** (equivalent calculated carbon-dioxide): concentration within a range of 400 to 8192 parts per million (ppm)

## To Do
- Create different icons for bad and good CO2 values 
- Switch from saving / loading dictionary to database
- Take lon and lat input from GET and return nearby values
- Introduce ML
- Add API Documentation

## Resources
- [Flask and Leaflet](https://programminghistorian.org/en/lessons/mapping-with-python-leaflet)

- [Adafruit CCS811 Air Quality Sensor Breakout - VOC and eCO2](https://www.adafruit.com/product/3566?gclid=CjwKCAjwk6P2BRAIEiwAfVJ0rLxm_lNaYtwD4zj__riHPa9Iyh2ksn7M8QShDgsPzd7igy4a4lvfMRoCHS0QAvD_BwE)