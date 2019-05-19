#!/bin/bash
sudo apt-get install curl
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y \
  python3.6 \
  python3-pip \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common
sudo apt-get install docker-ce docker-ce-cli containerd.io

curl http://mirror.dkd.de/apache/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz -o hadoop.tar.gz
tar -xzf  hadoop.tar.gz
