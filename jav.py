from flask import Flask
from flask import request
from flask import jsonify
from scrapinghub import ScrapinghubClient

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hellrld!"


@app.route('/thzgetdetail', methods=['GET'])
def getdetail():
    if request.method == 'GET':
        codelist = []
        apikey = '11befd9da9304fecb83dfa114d1926e9'
        client = ScrapinghubClient(apikey)
        project = client.get_project(252342)

        for job in list(project.jobs.iter_last(spider='javcode', state='finished')):
            codejob = job

        print(codejob['key'])
        lastcodejob = project.jobs.get(codejob['key'])

        for item in lastcodejob.items.iter():
            codelist.append(item['code'])
        print(codelist)
        return jsonify(codelist)
