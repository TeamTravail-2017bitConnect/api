import pymongo
from pymongo import MongoClient
import conf
import datetime
import time
import controller.http_request as hr

locationList1 = [
    {"truckId":3.0,"x":"35.655169","y":"139.665163"},
    {"truckId":3.0,"x":"35.656322","y":"139.664948"},
    {"truckId":3.0,"x":"35.658139","y":"139.664776"},
    {"truckId":3.0,"x":"35.659257","y":"139.664733"},
    {"truckId":3.0,"x":"35.659850","y":"139.664002"},
    {"truckId":3.0,"x":"35.660453","y":"139.662572"},
    {"truckId":3.0,"x":"35.661187","y":"139.662518"}
]
locationList2 = [
    {"truckId":3.0,"x":"35.661178","y":"139.663325"},
    {"truckId":3.0,"x":"35.660855","y":"139.663733"},
    {"truckId":3.0,"x":"35.660567","y":"139.664163"},
    {"truckId":3.0,"x":"35.660313","y":"139.664722"},
    {"truckId":3.0,"x":"35.659685","y":"139.665883"},
    {"truckId":3.0,"x":"35.660121","y":"139.666302"},
    {"truckId":3.0,"x":"35.660462","y":"139.666635"},
    {"truckId":3.0,"x":"35.660890","y":"139.666883"},
    {"truckId":3.0,"x":"35.661187","y":"139.667657"},
    {"truckId":3.0,"x":"35.661676","y":"139.667829"},
    {"truckId":3.0,"x":"35.661938","y":"139.668323"},
    {"truckId":3.0,"x":"35.662095","y":"139.668710"},
    {"truckId":3.0,"x":"35.662016","y":"139.669366"},
    {"truckId":3.0,"x":"35.661899","y":"139.669849"}
]

db = MongoClient(conf.MONGO_HOST, conf.MONGO_PORT)[conf.MONGO_DB]

def create_point(locations):
    for loc in locations:
        doc = loc
        todaydetail = datetime.datetime.today()
        doc["update_at"] = todaydetail.strftime("%Y-%m-%d %H:%M:%S")
        doc["address"] = hr.address(doc["x"],doc["y"])
        db.location_logs.insert(doc)
        time.sleep(2)

def remove():
    d = datetime.datetime(2017, 7, 30, 10)
    seq = [x["x"] for x in locationList1] + [x["x"] for x in locationList2]
    print seq
    db.location_logs.remove({"x":{"$in":seq}})

def updateStatus(bagId):
    bag = db.baggages.find_one({"baggageId":float(bagId)})
    bag["status"]="done"
    print bag
    db.baggages.update({"baggageId":bagId},bag)

def resetStatus(bagIds):
    bags = db.baggages.find({"baggageId":{"$in":bagIds}})
    for bag in bags:
        bag["status"]="delivering"
        db.baggages.update({"baggageId":bag["baggageId"]},bag)


if __name__ == "__main__":
    resetStatus([24.0,14.0,11.0])
    while(True):
        remove()
        updateStatus(24)
        create_point(locationList1)
        updateStatus(14)
        create_point(locationList2)
        updateStatus(11)
        time.sleep(4)
        resetStatus([24.0,14.0,11.0])
