from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicioSesion():
    return render_template('index.html')


@app.route('/SingUp')
def registro():
    return render_template('registro.html')


if __name__ == '__main__':
    app.run()
