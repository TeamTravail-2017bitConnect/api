import pymongo
from pymongo import MongoClient
import conf
import datetime
import time
import controller.http_request as hr

locationList = [
    {
    "truckId" : 3.0,
    "x": "35.6533953",
    "y": "139.6654639"
    },
        {
    "truckId" : 3.0,
    "x": "35.6612659",
    "y": "139.662633"
    },
        {
    "truckId" : 3.0,
    "x": "35.661873",
    "y": "139.6697843"
    }
]

db = MongoClient(conf.MONGO_HOST, conf.MONGO_PORT)[conf.MONGO_DB]

def create_point():
    for loc in locationList:
        doc = loc
        todaydetail = datetime.datetime.today()
        doc["update_at"] = todaydetail.strftime("%Y-%m-%d %H:%M:%S")
        doc["address"] = hr.address(doc["x"],doc["y"])
        print doc
        db.location_logs.insert(doc)
        time.sleep(2)


if __name__ == "__main__":
    while(True):
        create_point()
        d = datetime.datetime(2017, 7, 30, 10)
        db.location_logs.remove({"x":{"$in":["35.6533953","35.6612659","35.661873"]}})
