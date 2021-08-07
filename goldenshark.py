import json
import os
import subprocess

from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_url_path='')


PAGINATION = 20
BASE_PAGE = 1

mock_data = ["视觉显著性导向的图像压缩感知测量与重建,李艳灵",
             "图像分块压缩感知中的自适应测量率设定方法,武明虎",
             "联合时空特征的视频分块压缩感知重构,崔子冠",
             "基于PCA硬阈值收缩的平滑投影Landweber图像压缩感知重构,朱秀昌",
             "无线传感器网络中基于压缩感知的静止图像压缩方案研究,郑海波"]


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
                if search_word in mock_item:
                    output.append(mock_item)
        for i, out in enumerate(output):
            outdict[i] = out

        # Return CORS response
        return cors_response(outdict)
