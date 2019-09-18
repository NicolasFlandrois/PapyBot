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


# @app.route('/message/<msg>')
# def msg(msg):
#     # Get request/input from HTML/JS form & send to/use controls.py
#     # Get controls Reply: Sucess/Failure + Reply message & Send to JS to display
#     # IF Previous step == success Get parsed message, & send to Gmap API in JS, Else None

#     # return json.dumps(output)#return json file... to transmit to client cf how I did it in tests
#     return json.dumps({'Hello World'})    # Test Dev

@app.route("/message", methods=["GET"])
def create_entry():

    req = request.get_json()

    print(req) # Do Sthg

    res = make_response(jsonify({"message": "OK"}), 200)

    return res

if __name__ == "__main__":
    app.run(debug=True)
