from flask import Flask
from flask import request
from flask import jsonify
from scrapinghub import ScrapinghubClient
import subprocess

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hellrld!"


@app.route('/thzdetails', methods=['GET', 'POST'])
def getdetail():
    if request.method == 'GET':
        return 'Update. Ha Ha Ha, Get Details.'
    if request.method == 'POST':
        return 'POSTPOSTPOST...'


@app.route('/updatecode', methods=['POST'])
def updatecode():
    if request.method == 'POST':
        output = subprocess.check_output(
            ['git', '-C', r'/home/GoldenShark', 'pull'])
        return output
