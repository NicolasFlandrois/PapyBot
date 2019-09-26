#!/usr/bin/python3.7
# UTF8
# Date: Fri 16 Aug 2019 15:39:17 CEST
# Author: Nicolas Flandrois

from flask import Flask, render_template, request, jsonify, url_for, redirect
from form import QuestionForm
import json


app = Flask(__name__)


@app.route('/')
def index():
    form = QuestionForm()
    return render_template('index.html')


# @app.route('/msg', methods=['POST'])
# def msg():
#     # msg = request.form['user_request']
#         # Do sthg
#     # print('request: ', type(request.form))
#     # print('msg: ', type(msg))
#     print('Pouloulou')
#     send = {'result':f'Hello World {msg}'}
#     return jsonify(send)


# @app.route('/form')
# def form():

#     return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
