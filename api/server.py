# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   server.py
    Author:     Helyao
    Description:
        Support usable proxy-service by Flask API
-------------------------------------------------
    Change Logs:
    2017-06-02 3:00pm   create
-------------------------------------------------
"""
from flask import Flask
from store.operRedis import RedisOperater

app = Flask(__name__)
roper = RedisOperater()

@app.route('/')
def index():
    proxy = roper.getRandomUsable()
    return proxy

def run():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    run()
