import json
import os
import subprocess
import csv

from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_url_path='')


PAGINATION = 20
BASE_PAGE = 1

mock_data = []


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
    return app.send_static_file('goldenshark.html')


@app.route('/list', methods=['GET'])
def list_all():
    global mock_data
    if request.method == 'GET':
        output = []
        outdict = {}
        for mock_item in mock_data:
            output.append({"title": mock_item["title"],
                           "name": mock_item["name"],
                           "department": mock_item["department"],
                           "stage": mock_item["stage"]})
        for i, out in enumerate(output):
            outdict[i] = out

        # Return CORS response
        return cors_response(outdict)


@app.route('/search', methods=['GET'])
def list_search():
    if request.method == 'GET':
        output = []
        outdict = {}
        # Get para from URL like '/search?name=XX'
        # Get para from URL like '/search?makr=XX'
        # Get para from URL like '/search?word=XX'
        # if request.args.get("name"):
        #     search_name = request.args.get("name")
        #     filters = [("name", "=", [search_name])]
        # if request.args.get("makr"):
        #     search_makr = request.args.get("makr")
        #     filters = [("makr", "=", [search_makr])]
        if request.args.get("word"):
            search_word = request.args.get("word")
            for mock_item in mock_data:
                is_hit = 0
                if search_word in mock_item["title"]:
                    is_hit = 1
                if search_word in mock_item["name"]:
                    is_hit = 1
                if search_word in mock_item["department"]:
                    is_hit = 1
                if is_hit:
                    output.append({"title": mock_item["title"],
                                   "name": mock_item["name"],
                                   "department": mock_item["department"],
                                   "stage": mock_item["stage"]})
        for i, out in enumerate(output):
            outdict[i] = out

        print(outdict)
        # Return CORS response
        return cors_response(outdict)


def import_data():
    global mock_data
    with open('data.csv', encoding='utf-8-sig') as csvfile:
        cr = csv.DictReader(csvfile)
        for row in cr:
            mock_data.append(row)


if __name__ == '__main__':
    import_data()
    app.run(debug=True)
