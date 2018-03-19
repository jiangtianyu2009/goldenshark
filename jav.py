from flask import Flask
from flask import request
from flask import jsonify
from flask import send_from_directory
from scrapinghub import ScrapinghubClient
import subprocess
import os
import json

app = Flask(__name__)


@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/thzdetails', methods=['GET'])
def getdetail():
    if request.method == 'GET':
        with open(r'/home/GoldenShark/codelist.json', 'r') as thzfile:
            thzdict = json.load(thzfile)
            return jsonify(thzdict)


@app.route('/updatecode', methods=['POST'])
def performupdatecode():
    if request.method == 'POST':
        output = subprocess.check_output(
            ['git', '-C', r'/home/GoldenShark', 'pull', '-v'])
        return output


@app.route('/codelist', methods=['GET'])
def fetchcodelist():
    if request.method == 'GET':
        subprocess.Popen(['python3', r'/home/GoldenShark/codelist.py'])
        return 'update run fetch code list'
