from flask import Flask
from flask_pymongo import PyMongo
import urllib.parse as parser


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://"+parser.quote_plus("user")+":"+parser.quote_plus("password") +"@cluster-ugqjx.mongodb.net/analysis?retryWrites=true&w=majority"
app.config['MONGO_DBNAME'] = parser.quote_plus("user")
app.config['SECRET_KEY'] = parser.quote_plus("password")

mongo = PyMongo(app)
db = mongo.db
score_col = db["scores"]
dna_col = db["dnas"]

# print("MongoDB Database:", mongo.db)
