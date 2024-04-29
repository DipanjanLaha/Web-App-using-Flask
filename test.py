from flask import Flask, request, render_template
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Project"]
collection = db["flaskApp"]

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index(): # application code
    return render_template("index.html")

@app.route("/submit", methods = ["GET", "POST"])
def submit():
    username = request.form["Username"]
    password = request.form["Password"]
    collection.insert_one({"Username": username,"Password": password})
    data=collection.find()
    return render_template("dashboard.html", data=data)

if __name__ == '__main__':
    app.run()