from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origin': "*"}})


# hello world route
@app.route('/')
def hola_mundo():
    return "Hola mundo"


@app.route('/Log_in', methods=['GET'])
def inicioSesion():
    return "inicioSesion"


@app.route('/Sing_Up')
def registro():
    return "registro"


@app.route('/Menu_one', methods=["POST"])
def menu_one():
    print("OK")
    print(request.json)

    try:
        ask1 = request.json['answer_one']
        ask2 = request.json['answer_two']
        ask3 = request.json['answer_three']
        ask4 = request.json['answer_four']
        ask5 = request.json['answer_five']
        ask6 = request.json['answer_six']

        return jsonify({'message':
                           {'answer_one': ask1, 'answer_two': ask2,
                            'answer_three': ask3, 'answer_four': ask4,
                            'answer_five': ask5, 'answer_six': ask6}
                        })

    except Exception as error:
        print(error)

        return jsonify({'Error': 'Al recibir las respuestas del formulario'})


if __name__ == '__main__':
    app.run()
