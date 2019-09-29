
import json
from flask import Flask

import pymongo
import dns
from bson.json_util import dumps
from bson.json_util import loads
from bson.objectid import ObjectId

app = Flask(__name__)

client = pymongo.MongoClient('mongodb+srv://admin:ramHacks2019@hotwheels-gmjn8.gcp.mongodb.net/test')
# password = "ramHacks2019"
# print(client.Whips.HotWheels.count())
# print(dumps(client.Whips.HotWheels.find()))

db = client.Whips

collection = db.HotWheels
# a = db.collection.find({}, {_id:1}.map(function(item):return item._id; })

@app.route('/')
def index():
    return 'Server Works!'

@app.route('/year')
def year():
    year = dumps(collection.find({"year":"2018"}))
    return { "year": year}

@app.route('/car/<id>')
def get_car(_id):
    return {}

@app.route('/find/<coor>')
def find(coor):
    return {"location": dumps(collection.find({'location': coor}))}
