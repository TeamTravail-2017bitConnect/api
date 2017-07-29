import json
import utils
import http_request as hr
import falcon

class UserController(object):
    
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp, user_id):
        user = self.db.users.find_one({"id": float(user_id)})
        user = utils.removeId(user)
        resp.body = json.dumps(user, ensure_ascii=False)
        resp.append_header("Access-Control-Allow-Origin","*")

    def on_put(self, req, resp, user_id):
        doc = hr.toJson(req)
        user = self.db.users.find_one({"id": float(user_id)})
        doc["id"] = user["id"]
        doc["name"] = user["name"]
        self.db.users.update({"id": float(user_id)},doc)
        resp.status = falcon.HTTP_201
        resp.append_header("Access-Control-Allow-Origin","*")
        resp.body = "success"
