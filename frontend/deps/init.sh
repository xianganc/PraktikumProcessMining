#!/bin/bash

echo "PasswordAuthentication no" >> /etc/ssh/sshd_config
/usr/sbin/sshd -D &

python3 /webapp/server.py

while true; do
  sleep 1
done