import uuid 
import requests
import geocoder

from random import randint

def sendCO2(value, URL, lon, lat, name):
    data = {'lon': lon,
           'lat': lat,
           'name':name,
           'value': value} 

    return requests.post(url = URL, data = data)

def newpoint():
    return uniform(-180,180), uniform(-90, 90)

def newpointHouston():
    return uniform(29.5,30), uniform(-95, -96)

def getCO2():
    # Implement with CO2 module based code
    return None

def trackCO2(url, machine=True):
    if machine:
        myloc = geocoder.ip('me').latlng
        myloc = geocoder.ip('me').latlng
        lon = myloc[1]
        lat = myloc[0]
        while True:
            value = getCO2()
            sendCO2(value, url, lon, lat, id.hex)
    else:

        for x in range(1):
            # Values from CO2 module reports values
            # from 400 to 8192
            value = randint(400, 600)
            id = uuid.uuid4()
            lat, lon = newpointHouston()
            r = sendCO2(value, url, lon, lat, id.hex)
            print(r.text)
            
url = "https://co2nearme.herokuapp.com/receive"            
trackCO2(url = url, machine = False)