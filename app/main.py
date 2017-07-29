import falcon
import controller as c
from pymongo import MongoClient
import conf

db = MongoClient(conf.MONGO_HOST, conf.MONGO_PORT)[conf.MONGO_DB]
app = falcon.API()
app.add_route("/", c.HelloController())
app.add_route("/trucks/{truck_id}", c.TruckController(db))


if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()
