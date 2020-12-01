import json
import os
import subprocess

from flask import Flask, jsonify, request, send_from_directory
from scrapinghub import ScrapinghubClient

app = Flask(__name__, static_url_path='')

API_KEY = '11befd9da9304fecb83dfa114d1926e9'
PROJECT_ID = '252342'
PAGINATION = 10
BASE_PAGE = 1


def cors_response(orig_res):
    cors_res = jsonify(orig_res)
    cors_res.headers['Access-Control-Allow-Origin'] = '*'
    cors_res.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    cors_res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,\
        content-type'
    return cors_res


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route("/")
def index():
    return 'Hello, World!'


@app.route("/goldenshark")
def goldenshark():
    return app.send_static_file('index.html')


@app.route('/list', methods=['GET'])
def list_pagination():
    if request.method == 'GET':
        output = []
        outdict = {}
        para_page = BASE_PAGE
        client = ScrapinghubClient(API_KEY, use_msgpack=False)
        project = client.get_project(PROJECT_ID)
        for job in list(project.jobs.iter_last(
                spider='javorder', state='finished')):
            jav_order = job
        jav_order_job = project.jobs.get(jav_order['key'])

        # Get para from URL like '/list?page=INT'
        if request.args.get("page"):
            para_page = int(request.args.get("page"))
        for item in jav_order_job.items.list_iter(
                start=(para_page - 1) * PAGINATION,
                count=PAGINATION):
            output = item
        for i, out in enumerate(output):
            outdict[i] = out

        # Return CORS response
        return cors_response(outdict)


@app.route('/search', methods=['GET'])
def list_search():
    if request.method == 'GET':
        output = []
        outdict = {}
        client = ScrapinghubClient(API_KEY, use_msgpack=False)
        project = client.get_project(PROJECT_ID)
        for job in list(project.jobs.iter_last(
                spider='javorder', state='finished')):
            jav_order = job
        jav_order_job = project.jobs.get(jav_order['key'])

        # Get para from URL like '/search?name=XX'
        # Get para from URL like '/search?makr=XX'
        if request.args.get("name"):
            search_name = request.args.get("name")
            filters = [("name", "=", [search_name])]
        if request.args.get("makr"):
            search_makr = request.args.get("makr")
            filters = [("makr", "=", [search_makr])]
        for item in jav_order_job.items.iter(filter=filters):
            output.append(item)
        for i, out in enumerate(output):
            outdict[i] = out

        # Return CORS response
        return cors_response(outdict)
