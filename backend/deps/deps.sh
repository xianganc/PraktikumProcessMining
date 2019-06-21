#!/bin/bash
apt-get update ;
apt-get install -y \
  python3.6 \
  python3-pip \
  openssh-server \
  default-jre \

pip3 install pm4py flask