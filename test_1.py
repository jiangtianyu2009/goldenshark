import json
import os
import subprocess

from flask import Flask, jsonify, request, send_from_directory
from scrapinghub import ScrapinghubClient


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
    for item in jav_order_job.items.iter(count=10):
        output.append(item)

    print(output)

    return output


if __name__ == "__main__":
    fetchcodelist()
