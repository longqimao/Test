#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 22:49
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
if __name__=="__main__":
    app.run()


