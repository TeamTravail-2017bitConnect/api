import requests
import json

def address(x, y):
    url = "http://geoapi.heartrails.com/api/json?method=searchByGeoLocation&x={0}&y={1}".format(y, x)
    r = requests.get(url)
    body = r.json()
    print body["response"]
    loc = body["response"]["location"][0]
    return "{0} {1}{2}{3}".format(loc["postal"],tra(loc["prefecture"]),tra(loc["city"]), tra(loc["town"]))

def tra(st):
    return st.encode("utf-8")

if __name__=='__main__':
    print address('135.005213','35.001111')