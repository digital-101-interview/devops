#!/usr/bin/env python
# coding=utf-8
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_health():
    return jsonify({'status': 'OK'})

@app.route('/header', methods=['GET'])
def get_header():
    header = request.headers['host']
    return jsonify({'header': header})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)