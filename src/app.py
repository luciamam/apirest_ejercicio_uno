from flask import Flask,jsonify
from pymongo import MongoClient
from Productos.productos import productoslista




app=Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db=client['Apirest']
productos=db["productos"]





@app.route('/')
def home():
    #productos.insert_many(productoslista)
    return jsonify(productoslista)
    











if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")