from flask import Flask
from flask import request
from flask import jsonify
from scrapinghub import ScrapinghubClient

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hellrld!"


@app.route('/thzdetails', methods=['GET'])
def getdetail():
    if request.method == 'GET':
        return 'Ha Ha Ha, Get Details.'
