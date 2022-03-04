from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origin': "*"}})
# CORS(app, resources={r"/*":{'origin': 'http://localhost:8080/',"allow_header":"Access-Control-Allow-Origin"}})

# hello world route
@app.route('/')
def hola_mundo():
    return "Hola mundo"

@app.route('/Log_in', methods=['GET'])
def inicioSesion():
    return "inicioSesion"


"""
@app.route('/SingUp')
def registro():
    return render_template('registro.html')
"""

if __name__ == '__main__':
    app.run()
