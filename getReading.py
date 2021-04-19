#!/usr/bin/python3
import requests
import json

url = 'https://fia9c0dv5c.execute-api.us-west-1.amazonaws.com/default/simpleReading'

myobj ={
    'year': '2021',
    'month': '02',
    'day': '02',
    'hour': '14',
    'minute': '15',
    'timezone': 'America/Los_Angeles',
    'latitude': '37.7790262',
    'longitude': '-122.4199061'
}

x = requests.post(url, data = json.dumps(myobj))

print(x.content)

#print (json.dumps(myobj))
