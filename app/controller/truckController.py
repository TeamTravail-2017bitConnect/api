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
        truck["baggages"] = {}
        truck["baggages"]["done"] = [b for b in bags if b["status"]=="done"]
        truck["baggages"]["delivering"] = [b for b in bags if b["status"]=="delivering"]
        resp.body = json.dumps(truck, ensure_ascii=False)
