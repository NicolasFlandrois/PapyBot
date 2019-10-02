#!/usr/bin/python3.7
# UTF8
# Date: Wed 02 Oct 2019 16:51:11 CEST
# Author: Nicolas Flandrois

from flask import Flask, render_template, jsonify
from papybot.controls import *
import wikipedia

wikipedia.set_lang("fr")


app = Flask(__name__)


@app.route('/')
def index():
    greetings = Papy.randomchat(2, './papybot/data.json')
    return render_template('index.html', greetings=greetings)


@app.route('/msg/<string:msg>', methods=['GET'])
def msg(msg):
    parsed = Papy.parser(msg, "./papybot/data.json")
    wiki = Papy.wikipedia(parsed)
    papyChat = Papy.randomchat(wiki['status'], './papybot/data.json')
    gmapAPI = 'Pouloulou'

    if wiki['status'] is 1:
        send = {'status': wiki['status'], 'papy': papyChat,
                'summary': wiki['summary'],
                'url': wiki['url'], 'gmap': gmapAPI}
    else:
        send = {'status': wiki['status'], 'papy': papyChat,
                'error': wiki['error']}

    return jsonify(send)


if __name__ == "__main__":
    app.run(debug=True)
