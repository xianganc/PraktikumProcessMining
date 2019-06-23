#!/bin/bash
sudo apt-get install -y curl ;
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - ;
sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable" ;
sudo apt-get update ;
sudo apt-get install -y \
  python3.6 \
  python3-pip \
  apt-transport-https \
  ca-certificates \
  gnupg-agent \
  software-properties-common \
  docker-ce \
  docker-ce-cli \
  containerd.io \
  default-jre \
  ufw \
  iproute2

sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose ;
sudo chmod +x /usr/local/bin/docker-compose ;

curl http://mirror.dkd.de/apache/hadoop/common/hadoop-3.2.0/hadoop-3.2.0.tar.gz -o hadoop.tar.gz ;
tar -xzf  hadoop.tar.gz ;
mv hadoop-3.2.0 hadoop ;
rm hadoop.tar.gz ;


chmod +x ~/PraktikumProcessMining/integration/bin/*
chmod +x ~/PraktikumProcessMining/integration/deps/*

cp ~/PraktikumProcessMining/sshFile/aws_ssh ~/.ssh/id_rsa
sudo chmod 600 ~/.ssh/id_rsa

/bin/bash -c 'python3 ~/PraktikumProcessMining/integration/src/java_path.py'

sudo integration/deps/inject.sh

sudo docker build --tag processmining .

sudo docker-compose up --build -d

/bin/bash -c 'python3 ~/PraktikumProcessMining/integration/src/hadoop.py'


hadoop/bin/hdfs namenode -format
hadoop/sbin/start-dfs.sh
hadoop/bin/hdfs dfsadmin -report
hadoop/bin/hdfs dfs -mkdir -p /home
hadoop/bin/hdfs dfs -put data/annual2017.csv /home/annual2017.csv