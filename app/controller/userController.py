import json
import utils

class UserController(object):
    
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp, user_id):
        user = self.db.users.find_one({"id": float(user_id)})
        user = utils.removeId(user)
        resp.body = json.dumps(user, ensure_ascii=False)
        resp.append_header("Access-Control-Allow-Origin","*")

