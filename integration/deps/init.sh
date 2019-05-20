#!/bin/bash

curl http://mirror.dkd.de/apache/hadoop/common/hadoop-3.2.0/hadoop-3.2.0.tar.gz -o hadoop.tar.gz ;
tar -xzf  hadoop.tar.gz ;
mv hadoop-3.2.0 hadoop ;
rm hadoop.tar.gz ;

python /src/hadoop.py
/hadoop/bin/hdfs namenode -format

while true ; do
  sleep 1
done