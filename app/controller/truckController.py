import json
import pymongo

class TruckController(object):
    
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp, truck_id):
        trucks = self.db.trucks.find({"id": float(truck_id)})
        truck = [data for data in trucks][0]
        del truck["_id"]
        resp.body = json.dumps(truck)
