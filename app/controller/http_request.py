import requests
import json

def address(x, y):
    url = "http://geoapi.heartrails.com/api/json?method=searchByGeoLocation&x={0}&y={1}".format(y, x)
    r = requests.get(url)
    body = r.json()
    loc = body["response"]["location"][0]
    return "{0} {1}{2}{3}".format(loc["postal"],tra(loc["prefecture"]),tra(loc["city"]), tra(loc["town"]))

def tra(st):
    return st.encode("utf-8")

def toJson(req):
    body = req.stream.read()
    try:
        doc = json.loads(body)

    except (ValueError, UnicodeDecodeError):
        raise falcon.HTTPError(falcon.HTTP_753,
                                'Malformed JSON',
                                'Could not decode the request body. The '
                                'JSON was incorrect or not encoded as '
                                'UTF-8.')
    return doc


if __name__=='__main__':
    print address('135.005213','35.001111')