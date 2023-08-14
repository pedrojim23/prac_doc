from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Practica1 - creacion de una APIUrequest!'

@app.route('/holamundo/')
def holamundo():
    return 'HOLA MUNDO'

@app.route('/pruebadocker/')
def holadocker():
    return 'HOLA DOCKER'

@app.route('/holaluis/')
def holaluis():
    return 'HOLA LUIS!!!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
