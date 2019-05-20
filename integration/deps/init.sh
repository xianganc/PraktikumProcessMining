#!/bin/bash

adduser --system --shell /bin/bash --group --disabled-password hadoop
usermod -aG sudo hadoop
curl http://mirror.dkd.de/apache/hadoop/common/hadoop-3.2.0/hadoop-3.2.0.tar.gz -o hadoop.tar.gz ;
tar -xzf  hadoop.tar.gz ;
mv hadoop-3.2.0 hadoop ;
rm hadoop.tar.gz ;

python3 /src/hadoop.py
mkdir -p /home/hadoop/.ssh/
chown hadoop:hadoop /home/hadoop/.ssh/
ssh-keygen -t rsa -N "" -f /home/hadoop/.ssh/id_rsa
runuser -l hadoop -c 'ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@node-master'
/hadoop/bin/hdfs namenode -format
start_hadoop

while true ; do
  sleep 1
done