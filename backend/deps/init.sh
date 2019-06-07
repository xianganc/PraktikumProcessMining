#!/bin/bash

echo "PasswordAuthentication no" >> /etc/ssh/sshd_config
/usr/sbin/sshd -D &

python3 /src/src/main.py

while true; do
  sleep 1
done