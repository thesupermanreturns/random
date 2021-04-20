#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 23:35:37 2021

@author: pritee
"""

from flask import Flask, request

app = Flask(__name__)


@app.route('/hello_world')
def hello():
    return "Hello World"


@app.route('/add',methods=["GET"])
def add_GET():
    a = request.args.get('a')
    b = request.args.get('b')
    return str(int(a) + int(b))


#{
#    "a" : 5,
#    "b" : 4
#}


@app.route('/add',methods=["POST"])
def add_POST():
    data = request.get_json()
    a = data['a']
    b = data['b']
    return str(int(a) + int(b))
    


app.run()