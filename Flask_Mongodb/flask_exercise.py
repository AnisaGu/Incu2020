from pymongo import MongoClient
from flask_pymongo import PyMongo
from config import url
from flask import Flask, request, json, jsonify, render_template
from bson import json_util

print(url)

app = Flask(__name__, template_folder="my_templates")
app.config["MONGO_URI"] = url


json.dumps = json_util.dumps

mongo = PyMongo(app)

#check connection to database
@app.route("/check", methods=["GET"])
def get_interfaces():
    db_val = {"hostname": "Switch1"}
    result = mongo.db.interface.find(db_val)
    return jsonify(result)


@app.route("/<host_name>/interface.html", methods=["GET"])
def get_interface_html(host_name):
    db_val = {"hostname": host_name}
    result = mongo.db.interface.find(db_val)
    for s in result:
        res = s
    return render_template('index.html', result = res)


@app.route("/<host_name>/interface.json", methods=["GET"])
def get_interface_json(host_name):
    db_val = {"hostname": host_name}
    result = mongo.db.interface.find(db_val)
    return jsonify(result)


@app.route("/<host_name>/<interface_name>/details.json", methods=["GET"])
def get_int_json(host_name, interface_name):
    db_val = {"hostname": host_name, "interface": interface_name.replace('.', '/')}
    print(db_val)
    result = mongo.db.interface.find(db_val)
    return jsonify(result)


@app.route("/<host_name>/<interface_name>/details.html", methods=["GET"])
def get_int_html(host_name, interface_name):
    db_val = {"hostname": host_name, "interface": interface_name.replace('.', '/')}
    result = mongo.db.interface.find(db_val)
    for s in result:
        res = s
    return render_template("index.html", result = res)


if __name__ == '__main__':
    app.run()


mongo = PyMongo(app)