import pigpio
import json
from io import StringIO
import requests
import random

# pi = pigpio.pi()
# pi.set_PWM_dutycycle(1, 255)

def longLatMinutes(self, longtitude, latitude):
    print random.randint(1,25)

""" shelterLights returns the color the lights on the bus shelter should be given 
the bus shelter ID. Lights will turn blue if the bus is 2 minutes away"""
def shelterLights(self, shelterId):

  busList = []
  url = 'https://gateway.api.cloud.wso2.com:443/t/mystop/tcat/v1/rest/StopDepartures/Get/' + shelterId
  data = requests.get(url, headers={'Authorization': 'Bearer e5159b89-86c1-3cca-8412-59de037c674b'})
  io = StringIO(data.text)
  stopData = json.load(io)
  url2 = 'https://gateway.api.cloud.wso2.com/t/mystop/tcat/v1/rest/Routes/GetAllRoutes'
  data2 = requests.get(url, headers={'Authorization': 'Bearer e5159b89-86c1-3cca-8412-59de037c674b'})
  io2 = StringIO(data2.text)
  routeData = json.load(io2)

  for stop in stopData: 
    if (stop['StopId']==shelterId):
      for route in routeData:
        busList.append(route['Latitude'] + '/' + route['Longitude'])
        #Example x: 42.411239/-76.501395
        for x in busList:
          slashIndex = x.find('/')
          let longitude = x[0:slashIndex]
          let latitude = x[slashIndex+1:]
          let minutes= longLatMinutes(longitude, latitude)
          if minutes < 2: 
            return true 
          else:
            return false


#if stop id you entered equals the stop id of the url, then get a list of longitudes/latitudes 
#if for each bus, longLatMinutes(long,lat)<2 

      
"""possible ideas to get when the bus is 2 minutes away:
doesnt it depend on the specific bus and route
when a bus departs a bus shelter, how to extrapolate and see when the next one is coming?
"""



  

