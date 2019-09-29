import json
from flask import Flask

app = Flask(__name__)

data = [
    {
        "make": "Toyota",
        "model": "Altered Ego",
        "year": "2020",
        "location": "(1,2)",
        "reserved": True,
    },
    {
        "make": "Ford",
        "model": "Rigor Motor",
        "year": "2019",
        "location": "(1,4)",
        "reserved": True,
    },
    {
        "make": "Chevrolet",
        "model": "Torque Screw",
        "year": "2018",
        "location": "(1,5)",
        "reserved": False,
    },
    {
        "make": "Toyota",
        "model": "Altered Ego",
        "year": "2020",
        "location": "(1,1)",
        "reserved": False,
    },
    {
        "make": "Ford",
        "model": "Rigor Motor",
        "year": "2019",
        "location": "(1,3)",
        "reserved": False,
    },
    {
        "make": "Chevrolet",
        "model": "Torque Screw",
        "year": "2018",
        "location": "(1,6)",
        "reserved": False,
    },
    {
        "make": "Chevrolet",
        "model": "Torque Screw",
        "year": "2018",
        "location": "(2,1)",
        "reserved": False,
    },
    {
        "make": "Bugatti",
        "model": "Covelight",
        "year": "2017",
        "location": "(2,2)",
        "reserved": True,
    },
    {
        "make": "Bugatti",
        "model": "Covelight",
        "year": "2017",
        "location": "(2,3)",
        "reserved": True,
    },
    {
        "make": "Bugatti",
        "model": "Covelight",
        "year": "2017",
        "location": "(2,4)",
        "reserved": False,
    },
    {
        "make": "Lamborghini",
        "model": "Power Rocket",
        "year": "2016",
        "location": "(2,5)",
        "reserved": False,
    },
    {
        "make": "Lamborghini",
        "model": "Power Rocket",
        "year": "2016",
        "location": "(2,6)",
        "reserved": True,
    },
    {
        "make": "Lamborghini",
        "model": "Power Rocket",
        "year": "2016",
        "location": "(3,1)",
        "reserved": False,
    },
    {
        "make": "Honda",
        "model": "Rocket Box",
        "year": "2015",
        "location": "(3,2)",
        "reserved": False,
    },
    {
        "make": "Honda",
        "model": "Rocket Box",
        "year": "2015",
        "row": "(3,3)",
        "reserved": False,
    },
    {
        "make": "Honda",
        "model": "Rocket Box",
        "year": "2015",
        "location": "(3,4)",
        "reserved": False,
    },
]


@app.route("/")
def index():
    return "Server Works!"


@app.route("/car/<id>")
def get_car(_id):
    return {}


@app.route("/find/<coor>")
def find(coor):
    car = [x for x in data if data["location"] == coor]
    return {"location": car}
