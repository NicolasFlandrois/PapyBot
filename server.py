#!/usr/bin/python3.7
# UTF8
# Date: Fri 16 Aug 2019 15:39:17 CEST
# Author: Nicolas Flandrois

from flask import Flask, render_template, request, jsonify, make_response
import json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/message/<string:msg>/')
def create_entry(msg):
        # Do sthg
    print('Pouloulou')
    return 'Hello World'


if __name__ == "__main__":
    app.run(debug=True)
