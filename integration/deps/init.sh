#!/bin/bash

useradd -p hadoop hadoop
usermod -aG sudo hadoop
curl http://mirror.dkd.de/apache/hadoop/common/hadoop-3.2.0/hadoop-3.2.0.tar.gz -o hadoop.tar.gz ;
tar -xzf  hadoop.tar.gz ;
mv hadoop-3.2.0 hadoop ;
rm hadoop.tar.gz ;

python3 /src/hadoop.py
runuser -l hadoop -c 'sh-keygen -t rsa -N "" -f ~/.ssh/id_rsa'
runuser -l hadoop -c 'ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@node-master'
/hadoop/bin/hdfs namenode -format
start_hadoop

while true ; do
  sleep 1
done