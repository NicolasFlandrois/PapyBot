#!/usr/bin/python3.7
# UTF8
# Date: Fri 16 Aug 2019 15:39:17 CEST
# Author: Nicolas Flandrois

from flask import Flask, render_template, request, jsonify, url_for
import json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/msg/<string:msg>', methods=['GET'])
def msg(msg):
    # Do sthg
    print('msg: ', type(msg))
    print('Pouloulou')
    send = {'res': f'Hello World {msg}'}
    print(send)
    return jsonify(send)
    # return send['res']
    # return send


if __name__ == "__main__":
    app.run(debug=True)
