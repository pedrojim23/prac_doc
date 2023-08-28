from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Practica1- APIrequest!'

@app.route('/holamundo/')
def holamundo():
    return 'Hola mundo'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
