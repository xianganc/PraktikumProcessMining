#!/bin/bash

useradd -p hadoop hadoop
usermod -aG sudo hadoop
curl http://mirror.dkd.de/apache/hadoop/common/hadoop-3.2.0/hadoop-3.2.0.tar.gz -o hadoop.tar.gz ;
tar -xzf  hadoop.tar.gz ;
mv hadoop-3.2.0 hadoop ;
rm hadoop.tar.gz ;

python3 /src/hadoop.py
mkdir -p /home/hadoop/.ssh/
cp /shared/ssh/aws_ssh /home/hadoop/.ssh/id_rsa
chown -R hadoop:hadoop /home/hadoop/.ssh/
/hadoop/bin/hdfs namenode -format
start_hadoop

while true ; do
  sleep 1
done