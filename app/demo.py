import pymongo
from pymongo import MongoClient
import conf
import datetime
import time
import controller.http_request as hr

locationList1 = [
    {"trackId":3.0,"x":"35.655169","y":"139.665163"},
    {"trackId":3.0,"x":"35.656322","y":"139.664948"},
    {"trackId":3.0,"x":"35.658139","y":"139.664776"},
    {"trackId":3.0,"x":"35.659257","y":"139.664733"},
    {"trackId":3.0,"x":"35.659850","y":"139.664002"},
    {"trackId":3.0,"x":"35.660453","y":"139.662572"},
    {"trackId":3.0,"x":"35.661187","y":"139.662518"}
]
locationList2 = [
    {"trackId":3.0,"x":"35.661178","y":"139.663325"},
    {"trackId":3.0,"x":"35.660855","y":"139.663733"},
    {"trackId":3.0,"x":"35.660567","y":"139.664163"},
    {"trackId":3.0,"x":"35.660313","y":"139.664722"},
    {"trackId":3.0,"x":"35.659685","y":"139.665883"},
    {"trackId":3.0,"x":"35.660121","y":"139.666302"},
    {"trackId":3.0,"x":"35.660462","y":"139.666635"},
    {"trackId":3.0,"x":"35.660890","y":"139.666883"},
    {"trackId":3.0,"x":"35.661187","y":"139.667657"},
    {"trackId":3.0,"x":"35.661676","y":"139.667829"},
    {"trackId":3.0,"x":"35.661938","y":"139.668323"},
    {"trackId":3.0,"x":"35.662095","y":"139.668710"},
    {"trackId":3.0,"x":"35.662016","y":"139.669366"},
    {"trackId":3.0,"x":"35.661899","y":"139.669849"}
]

db = MongoClient(conf.MONGO_HOST, conf.MONGO_PORT)[conf.MONGO_DB]

def create_point(locations):
    for loc in locations:
        doc = loc
        todaydetail = datetime.datetime.today()
        doc["update_at"] = todaydetail.strftime("%Y-%m-%d %H:%M:%S")
        doc["address"] = hr.address(doc["x"],doc["y"])
        print doc
        db.location_logs.insert(doc)
        time.sleep(4)

def remove():
    d = datetime.datetime(2017, 7, 30, 10)
    db.location_logs.remove({"x":{"$in":[]}})

def updateStatus(bagId):
    bag = db.baggages.find_one({"baggageId":float(bagId)})
    bag["status"]=="done"
    db.baggages.update({"baggageId":float(bagId)},bag)

def resetStatus(bagIds):
    bags = db.baggages.find({"baggageId":{"$in":bagIds}})
    for bag in bags:
        bag["status"]=="delivering"
        db.baggages.update({"baggageId":float(bag["baggageId"])},bag)

if __name__ == "__main__":
    while(True):
        updateStatus(24)
        create_point(locationList1)
        updateStatus(14)
        create_point(locationList2)
        updateStatus(11)
        time.sleep(4)
        resetStatus(24,14,11)

