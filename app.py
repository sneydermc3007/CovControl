from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicioSesion():
    return render_template('index.html')


"""
@app.route('/Sing Up')
def Registro():
    return 'Registro de Usuarios'
"""

if __name__ == '__main__':
    app.run(debug=True)
