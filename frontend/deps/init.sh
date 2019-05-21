#!/bin/bash

service apache2 start
python3 /src/app.py

while true; do
  sleep 1
done