import json
import os
import subprocess

from flask import Flask, jsonify, request, send_from_directory
from scrapinghub import ScrapinghubClient


API_KEY = '11befd9da9304fecb83dfa114d1926e9'
PROJECT_ID = '252342'


def fetchcodelist():
    client = ScrapinghubClient(API_KEY)
    project = client.get_project(PROJECT_ID)

    for job in list(project.jobs.iter_last(
            spider='javdetail', state='finished')):
        javjob = job

    print(javjob['key'])
    job = project.jobs.get(javjob['key'])

    output = []
    for i, item in enumerate(job.items.iter()):
        output.append({'code': item['code'], 'date': item['date']})
    output.sort(key=lambda x: x['date'], reverse=True)
    print(output[0:100])

    return output


if __name__ == "__main__":
    fetchcodelist()
