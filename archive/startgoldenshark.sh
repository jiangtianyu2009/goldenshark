#!/bin/bash

cd /home/GoldenShark/

. venv/bin/activate

gunicorn -w 4 -b 127.0.0.1:4000 jav:app --reload --daemon
