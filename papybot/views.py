#!/usr/bin/python3.7
# UTF8
# Date: Fri 16 Aug 2019 15:38:48 CEST 
# Author: Nicolas Flandrois


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

if __name__ == "__main__":
    app.run()
