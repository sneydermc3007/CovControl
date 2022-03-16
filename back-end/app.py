    from urllib import response
    from flask import Flask, jsonify, request, Response
    from flask_pymongo import PyMongo
    from bson import json_util
    from bson.objectid import ObjectId

    from werkzeug.security import generate_password_hash, check_password_hash

    app = Flask(__name__)

    app.secret_key = 'myawesomesecretkey'

    app.config['MONGO_URI'] = 'mongodb://database/pythonmongodb'

    mongo = PyMongo(app)

    #REGISTOR DE USUARIOS U.CATOLICA
    @app.route('/users', methods=['POST'])
    def create_user():
        # Receiving Data
        username = request.json['username']  #-->ES LA CEDULA
        email = request.json['email']
        password = request.json['password']
        
        if username and email and password:
            mongo.db.users.insert(
                {'username': username, 'email': email, 'password':password}
            )
            response = {
                'username': username,
                'email': email,
                'password': password
            }
            return response
        else:
            return {'message': 'received'}




    if __name__ == "__main__":
        app.run(debug=True)