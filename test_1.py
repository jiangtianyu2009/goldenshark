import json
import os
import subprocess

import requests
from flask import Flask, jsonify, request, send_from_directory
from scrapinghub import ScrapinghubClient

NAME_LIST_URL = ('https://raw.githubusercontent.com/bsonnier/'
                 'bsonnier.github.io/master/docs/namelist')
API_KEY = '11befd9da9304fecb83dfa114d1926e9'
PROJECT_ID = '252342'


def fetchcodelist():
    client = ScrapinghubClient(API_KEY, use_msgpack=False)
    project = client.get_project(PROJECT_ID)

    for jav_order_job in list(project.jobs.iter_last(
            spider='javorder', state='finished')):
        javjob = jav_order_job

    print(javjob['key'])
    jav_order_job = project.jobs.get(javjob['key'])

    output = []
    for item in jav_order_job.items.list_iter(start=5, count=3):
        output.append(item)

    filters = [("name", "=", ['楓カレン'])]
    for item in jav_order_job.items.iter(count=10, filter=filters):
        print(item)

    namelist = requests.get(NAME_LIST_URL).text.split()
    print(namelist)

    return output


if __name__ == "__main__":
    fetchcodelist()
