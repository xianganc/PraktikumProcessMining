#!/bin/bash

echo "PasswordAuthentication no" >> /etc/ssh/sshd_config
/usr/sbin/sshd -D &


python3 /var/www/server.py

echo "LEFT PYTHON SCRIPT! RESTARTING"