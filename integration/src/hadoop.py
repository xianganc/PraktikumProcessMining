import subprocess

ip = subprocess.check_output(["./integration/bin/docker_ip"]).decode('utf-8').split()[-1]
print(ip)
#print("There are some setup questions incoming")
config = """<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://%s:9000</value>
    </property>
</configuration>""" % (ip)
with open("./hadoop/etc/hadoop/core-site.xml","w") as configfile:
  configfile.write(config)
config = """<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>"""
with open("./hadoop/etc/hadoop/hdfs-site.xml","w") as configfile:
  configfile.write(config)
#config = """<configuration>
#  <property>
#          <name>yarn.acl.enable</name>
#          <value>0</value>
#  </property>
#
#   <property>
#          <name>yarn.resourcemanager.hostname</name>
#          <value>node-master</value>
#  </property>
#  <property>
#          <name>yarn.nodemanager.resource.memory-mb</name>
#          <value>512</value>
#  </property>
#
#   <property>
#          <name>yarn.scheduler.maximum-allocation-mb</name>
#          <value>512</value>
#  </property>
#
#   <property>
#          <name>yarn.scheduler.minimum-allocation-mb</name>
#          <value>64</value>
#  </property>
#
#   <property>
#          <name>yarn.nodemanager.vmem-check-enabled</name>
#          <value>false</value>
#  </property>
#  </configuration>"""
#with open("./hadoop/etc/hadoop/yarn-site.xml","w") as configfile:
  #configfile.write(config)
java_path = subprocess.check_output("./integration/bin/check_java").decode("utf-8").split()[-1][:-8]
with open("./hadoop/etc/hadoop/hadoop-env.sh","a") as envfile:
  envfile.write("export JAVA_HOME="+java_path)
with open("/etc/hosts","a") as hosts:
  hosts.writelines(["%s node-master \n" % ip])