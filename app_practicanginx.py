from flask import Flask
import requests
import json

app = Flask(__name__)

contador = 0

@app.route('/')
def index():
    return 'Practica1- APIrequest!'

@app.route('/holamundo/')
def holamundo():
    return 'Hola mundo'

@app.route('/pruebadocker/')
def holadocker():
    return 'Hola docker'

@app.route('/nginx/')
def nginx():
    return '<body bgcolor=ff000> <h1>ENDPOINT ACTIVADO NGINX</h1> </body>'

@app.route('/count/')
def count():
    global contador
    contador +=1
    return f'Acceso a count - Clicks realizados: {contador}'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
