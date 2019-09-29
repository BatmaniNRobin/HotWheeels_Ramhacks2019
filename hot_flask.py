
import json
from flask import Flask

import pymongo
import dns
from bson.json_util import dumps

app = Flask(__name__)

client = pymongo.MongoClient('mongodb+srv://hotwheels-gmjn8.gcp.mongodb.net/test')
# password = "ramHacks2019"

db = client.Whips

collection = db['HotWheels']

# a = db.collection.find({}, {_id:1}.map(function(item):return item._id; })

@app.route('/')
def index():
    return 'Server Works!'

@app.route('/great')
def say_hello():
    return 'Hello from server'
# make endpoints

@app.route('/cars')
def cars():
    return { "cars": db._id_ }

@app.route('/car/<id>')
def get_car(id):
    return {}

