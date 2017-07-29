import json

class HelloController(object):

    def on_get(self, req, resp):
        msg = {
            "message": "Welcome to the Falcon"
        }
        resp.body = json.dumps(msg)
