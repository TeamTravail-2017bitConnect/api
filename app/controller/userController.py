import json

class UserController(object):
    
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp, user_id):
        users = self.db.users.find_One({"id": float(user_id)})
        truck = [data for data in trucks][0]
        resp.body = json.dumps(bs, ensure_ascii=False)
        resp.append_header("Access-Control-Allow-Origin","*")

