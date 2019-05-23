#!/bin/bash

echo "PasswordAuthentication no" >> /etc/ssh/sshd_config
/usr/sbin/sshd -D &
service apache2 start
python3 /src/app.py

while true; do
  sleep 1
done