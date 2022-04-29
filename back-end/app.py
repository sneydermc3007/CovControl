from flask import Flask, jsonify, request
from flask_cors import CORS

import json
from multiprocessing import set_forkserver_preload
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origin': "*"}})

db = SQLAlchemy(app)
Marshmallow(app)
ma = Marshmallow(app)

class registro(db.Model): #Falta el dato de verificacion
    id = db.Column(db.Integer, primary_key= True)
    firstname = db.Column(db.String(50))
    secondname = db.Column(db.String(100))
    lastname = db.Column(db.String(50))
    secondlastname = db.Column(db.String(50))
    born = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    number = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))

    #Falta el dato de verificacion y el id sobra
    def __init__(self, id, firstname, sencondname, lastname,
                    secondlastname, born,gender,number,email, password):
        self.id = id
        self.firstname = firstname
        self.secondname =  sencondname
        self.lastname = lastname
        self.secondlastname = secondlastname
        self.born = born
        self.gender = gender
        self.number = number
        self.email = email
        self.password = password


db.create_all()

class RegistroSchema(ma.Schema):
    class Meta:
        fields = ('id', 'firstname', 'secondname', 'lastname', 'secondlastname',
                    'born', 'gender', 'number', 'email', 'password')

registro_schema = RegistroSchema()
registros_schema = RegistroSchema(many=True)

@app.route('/Sing_Up', methods=["POST"])
def create_user():
    #  Receiving datas
    print("Ok")
    print(request.json)

    try:
        first_name = request.json['first_name']
        secondname = request.json['second_name']
        first_surname = request.json['first_surname']
        second_surname = request.json['second_surname']
        born = request.json['born']
        sex = request.json['sex']
        number = request.json['number']
        email = request.json['email']
        password = request.json['password']

        return jsonify({'message': 'received'})

    except Exception as ex:
        print(ex)
        return jsonify({'Error': 'El procesamiento de datos'})

@app.route('/Log_in', methods=["POST"])
def login():
    print(request.json)

    try:
        email = request.json['email']
        password = request.json['pass']

        return jsonify({'message': 'received'})

    except Exception as ex:
        print(ex)
        return jsonify({'Error': 'En el momento de traer el usuario'})

def pag_no_found(error):
    print(error)
    return "<h1> La pagina que intentas acceder no existe, verifica la ruta! </h1>"


if __name__ == "__main__":
    app.register_error_handler(404, pag_no_found)
    app.run(debug=True)