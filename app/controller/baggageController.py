import json

class BaggageController(object):
    
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp):
        baggages = self.db.baggages.find()
        baggage = [data for data in baggages][0]
        del baggage["_id"]
        resp.body = json.dumps(baggage)
