import json
import os
import subprocess

from flask import Flask, jsonify, request, send_from_directory
from scrapinghub import ScrapinghubClient

app = Flask(__name__, static_url_path='')

API_KEY = '11befd9da9304fecb83dfa114d1926e9'
PROJECT_ID = '252342'


@app.route("/")
def index():
    # return app.send_static_file('index.html')
    return 'Hello, World!'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/codelist', methods=['GET'])
def fetchcodelist():
    if request.method == 'GET':
        client = ScrapinghubClient(API_KEY)
        project = client.get_project(PROJECT_ID)

        for jav_order_job in list(project.jobs.iter_last(
                spider='javorder', state='finished')):
            javjob = jav_order_job

        print(javjob['key'])
        jav_order_job = project.jobs.get(javjob['key'])

        for item in jav_order_job.items.iter(count=1):
            output = item

        return output


def corsresponse(origres):
    corsres = jsonify(origres)
    corsres.headers['Access-Control-Allow-Origin'] = '*'
    corsres.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    corsres.headers['Access-Control-Allow-Headers'] = 'x-requested-with,\
        content-type'
    return corsres
