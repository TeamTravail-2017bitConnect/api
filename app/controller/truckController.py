# -*- coding: utf-8 -*-
import json
import pymongo
import utils
import baggageController as bc

class TruckController(object):
    
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp, truck_id):
        trucks = self.db.trucks.find({"id": float(truck_id)})
        truck = [data for data in trucks][0]
        baggageIds = [{"baggageId":data} for data in truck['baggageIds']]
        baggages = self.db.baggages.find({"$or": baggageIds})
        bags = bc.BaggageController.toData(baggages)
        del truck["_id"]
        
        bagKey = "baggages"
        doneKey = "done"
        deliverKey = "delivering"
        truck[bagKey] = {}
        truck[bagKey][doneKey] = [b for b in bags if b["status"]==doneKey]
        truck[bagKey][deliverKey] = [b for b in bags if b["status"]==deliverKey]
        truck["progressRate"] = float(len(truck[bagKey][doneKey]))/(len(truck[bagKey][doneKey]) + len(truck[bagKey][deliverKey]))
        resp.body = json.dumps(truck, ensure_ascii=False)
