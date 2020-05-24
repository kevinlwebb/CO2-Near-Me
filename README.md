# CO<sub>2</sub> Near Me
### CO<sub>2</sub> Map and API

## Overview
**CO<sub>2</sub> Near Me** is a simple map with an accompanying API. Embedded Devices can send data to the provided endpoint, and the map will display the location alongisde the CO<sub>2</sub> value.  As the the application is built out, the API will be able to take in longitude and latitude values and give back specific values for the area.

## Terms
- **eCO<sub>2</sub>** (equivalent calculated carbon-dioxide) concentration within a range of 400 to 8192 parts per million (ppm)

## To Do
- Create different icons for bad and good CO2 values 
- Switch from saving / loading dictionary to database
- Take lon and lat input from GET and return nearby values
- Introduce ML

## Resources
- [Flask and Leaflet](https://programminghistorian.org/en/lessons/mapping-with-python-leaflet)

- [Adafruit CCS811 Air Quality Sensor Breakout - VOC and eCO2](https://www.adafruit.com/product/3566?gclid=CjwKCAjwk6P2BRAIEiwAfVJ0rLxm_lNaYtwD4zj__riHPa9Iyh2ksn7M8QShDgsPzd7igy4a4lvfMRoCHS0QAvD_BwE)