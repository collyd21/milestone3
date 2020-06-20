import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'milestone-3'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_users')
def get_users():
    return render_template("users.html", users=mongo.db.users.find())


@app.route('/permits')
def permits():
    return render_template("permits.html", permits=mongo.db.permits.find().sort("date"))


@app.route('/new_permit')
def new_permit():
    return render_template("new_permit.html")


@app.route('/add_permit', methods=['POST'])
def add_permit():
    permits =  mongo.db.permits
    permits.insert(request.form.to_dict())
    return render_template("permits.html", permits=mongo.db.permits.find())


@app.route('/view_permit')
def view_permit():
    return render_template("view_permit.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
