from urllib import response
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util 
from bson.objectid import ObjectId
from pymongo import MongoClient

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

#app.secret_key = 'myawesomesecretkey'

#app.config['MONGO_URI'] = 'mongodb://database/pythonmongodb'

#mongo = PyMongo(app)


@app.route('/registro', methods = ['POST'])
def create_user():
    #Receiving data
    username = request.json['username'] #---->Esta es la cedula
    password = request.json['password']
    email = request.json['email']
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    gender = request.json['gender']
    number = request.json['number']
    program = request.json['program]

    return {'message': 'received'}


@app.route('/login', methods = ['GET'])
def login():
    #Looking for data
    username = request.json['username'] #---->Esta es la cedula
    password = request.json['password']

    return {'message': 'received'}
###GET,PUT, DELETE


    

""""
    if username and password and email:
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert(
            {'username': username, 'password': hashed_password, 'email': email}
        )
        response = {
            'id': str(id),
            'username': username,
            'password': hashed_password,
            'email': email,
            #firstname = request.json['firstname]
            #lastname = request.json['lastname']
            #gender = request.json['gender]
            #number = request.json['number']
        }
        return response

    else:
        return {'message': 'received'}




    


"""

if __name__ == "__main__":
        app.run(debug=True)
