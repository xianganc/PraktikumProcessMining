#!/bin/bash

python3 /src/app.py
service apache2 start

while true; do
  sleep 1
done