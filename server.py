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


@app.route('/msg/<string:msg>')
def msg(msg):
    # msg = request.form['user_request']
        # Do sthg
    # print('request: ', type(request.form))
    print('msg: ', type(msg))
    print('Pouloulou')
    send = {'result':f'Hello World {msg}'}
    return jsonify(send)


if __name__ == "__main__":
    app.run(debug=True)
