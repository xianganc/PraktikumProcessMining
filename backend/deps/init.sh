#!/bin/bash

echo "PasswordAuthentication no" >> /etc/ssh/sshd_config
/usr/sbin/sshd -D &

useradd hadoop

sleep 35

python3 /src/src/main.py

echo "LEFT PYTHON SCRIPT! RESTARTING"

