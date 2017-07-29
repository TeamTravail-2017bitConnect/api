import json
import utils

class BaggageController(object):
    
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp):
        baggages = self.db.baggages.find()
        bs = self.toData(baggages)
        resp.body = json.dumps(bs, ensure_ascii=False)
        resp.append_header("Access-Control-Allow-Origin","*")

    @staticmethod
    def toData(baggages):
         return [utils.removeId(data) for data in baggages]