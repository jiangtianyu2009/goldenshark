#!/bin/bash

git -C /home/bsonnier.github.io/ add -A

git -C /home/bsonnier.github.io/ commit -m "$(date)"

git -C /home/bsonnier.github.io/ push
