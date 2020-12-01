#!/bin/bash

git -C /home/bsonnier.github.io/ pull

git -C /home/bsonnier.github.io/ add -A

git -C /home/bsonnier.github.io/ commit -m "$(date)" -m "$(git -C /home/bsonnier.github.io/ status)"

git -C /home/bsonnier.github.io/ push
