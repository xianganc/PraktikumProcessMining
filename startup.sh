#!/bin/bash
sudo apt-get install curl
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y \
  python3.6 \
  python3-pip \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common \
  git \
  docker-ce \
  docker-ce-cli \
  containerd.io

git clone https://github.com/xianganc/PraktikumProcessMining.git
cd PraktikumProcessMining/integration
curl http://mirror.dkd.de/apache/hadoop/common/hadoop-3.2.0/hadoop-3.2.0.tar.gz -o hadoop.tar.gz
tar -xzf  hadoop.tar.gz
mv hadoop-3.2.0 hadoop
