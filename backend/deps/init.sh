#!/bin/bash

echo "PasswordAuthentication no" >> /etc/ssh/sshd_config
/usr/sbin/sshd -D &

python3 /src/src/main.py

echo "LEFT PYTHON SCRIPT! RESTARTING"