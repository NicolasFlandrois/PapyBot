#!/usr/bin/python3.7
# UTF8
# Date: Fri 16 Aug 2019 15:39:17 CEST
# Author: Nicolas Flandrois

from flask import Flask, render_template, request, jsonify, url_for
from papybot.controls import *
import json
import wikipedia

wikipedia.set_lang("fr")


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/msg/<string:msg>', methods=['GET'])
def msg(msg):
    parsed = Papy.parser(msg, "./papybot/data.json")
    wiki = Papy.wikipedia(parsed)
    papyChat = Papy.randomchat(wiki['status'], './papybot/data.json')
    gmapAPI = 'pouloulou'

    if wiki['status'] is 1:
        send = {'papy': papyChat, 'summary': wiki['summary'],
                'url': wiki['url'], 'gmap': gmapAPI, }
    else:
        send = {'papy': papyChat, 'error': wiki['error']}

    return jsonify(send)


if __name__ == "__main__":
    app.run(debug=True)
