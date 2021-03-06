# -*- coding: utf-8 -*-
import json
import pymongo
import utils
import baggageController as bc
import falcon
import datetime
import http_request as hr

bagKey = "baggages"
doneKey = "done"
deliverKey = "delivering"
redeliverKey = "redelivery"

class TruckController(object):
    
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp, truck_id):
        truck = self.db.trucks.find_one({"id": float(truck_id)})
        truck = self.createBaggage(truck)
        del truck["_id"]
        del truck["baggageIds"]
        truck = self.createHistory(truck)
        
        truck["progressRate"] = self.createProgress(truck)
        resp.body = json.dumps(truck, ensure_ascii=False)
        resp.append_header("Access-Control-Allow-Origin","*")

    def createProgress(self, truck):
        done = len(truck[bagKey][doneKey])
        deliver = len(truck[bagKey][deliverKey])
        redeliver = len(truck[bagKey][redeliverKey])
        rate = float(done)/(done + deliver + redeliver)
        return float('%03.3f' % rate)
    
    def createBaggage(self, truck):
 
        baggageIds = [{"baggageId":data} for data in truck['baggageIds']]
        baggages = self.db.baggages.find({"$or": baggageIds})
        bags = bc.BaggageController.toData(baggages)

        truck[bagKey] = {}
        truck[bagKey][doneKey] = [b for b in bags if b["status"]==doneKey]
        truck[bagKey][deliverKey] = [b for b in bags if b["status"]==deliverKey]
        truck[bagKey][redeliverKey] = [b for b in bags if b["status"]==redeliverKey]
        return truck

    def createHistory(self, truck):
        id = truck["id"]
        history = self.db.location_logs.find({"truckId":float(id)}).sort("update_at", pymongo.DESCENDING).limit(20)
        truck["locationHistory"] = [utils.removeId(x) for x in history]
        return truck

    def on_put(self, req, resp, truck_id):
        doc = hr.toJson(req)
        doc["truckId"] = truck_id
        todaydetail = datetime.datetime.today()
        doc["update_at"] = todaydetail.strftime("%Y-%m-%d %H:%M:%S")
        doc["address"] = hr.address(doc["x"],doc["y"])
        self.db.location_logs.insert(doc)

        resp.status = falcon.HTTP_201
        resp.append_header("Access-Control-Allow-Origin","*")
