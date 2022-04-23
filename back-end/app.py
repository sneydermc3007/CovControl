from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origin': "*"}})


@app.route('/Sing_Up', methods=["POST"])
def create_user():
    #  Receiving datas
    print("Ok")
    print(request.json)
    #   print(request.json['test'])

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
        verify_password = request.json['verify_password']

        return jsonify({'message': 'received'})

    except Exception as ex:
        print(ex)
        return jsonify({'Error': 'El procesamiento de datos'})


@app.route('/Log_in', methods=['POST'])
def login():
    # Looking for data

    correo = request.json['email']
    password = request.json['pass']

    return jsonify({'message': 'received'})


def pag_no_found(error):
    print(error)
    return "<h1> La pagina que intentas acceder no existe, verifica la ruta! </h1>"


if __name__ == "__main__":
    app.register_error_handler(404, pag_no_found)
    app.run(debug=True)
