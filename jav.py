from flask import Flask
from flask import request
from flask import jsonify
from flask import send_from_directory
from scrapinghub import ScrapinghubClient
import subprocess
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Test Test Test update. Hellrld!"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/thzdetails', methods=['GET', 'POST'])
def getdetail():
    if request.method == 'GET':
        return 'Test update. Update. Ha Ha Ha, Get Details.'
    if request.method == 'POST':
        return 'POSTPOSTPOST...'


@app.route('/updatecode', methods=['POST'])
def updatecode():
    if request.method == 'POST':
        output = subprocess.check_output(
            ['git', '-C', r'/home/GoldenShark', 'pull'])
        return output


@app.route('/codelist', methods=['GET'])
def fetchcodelist():
    if request.method == 'GET':
        codelist = []
        apikey = '11befd9da9304fecb83dfa114d1926e9'
        client = ScrapinghubClient(apikey)
        project = client.get_project(252342)

        for job in list(project.jobs.iter_last(spider='myspider', state='finished')):
            codejob = job

        print(codejob['key'])
        lastcodejob = project.jobs.get(codejob['key'])

        for item in lastcodejob.items.iter():
            codelist.append(item)
        print(codelist)
        return jsonify(codelist)
