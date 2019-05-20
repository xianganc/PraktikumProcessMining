import subprocess


print("There are some setup questions incoming")
config = """<?xml version="1.0" encoding="UTF-8"?>
  <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
  <configuration>
      <property>
          <name>fs.default.name</name>
          <value>hdfs://node-master:9000</value>
      </property>
  </configuration>"""
with open("/hadoop/etc/hadoop/core-site.xml","w") as configfile:
  configfile.write(config)
config = """<configuration>
  <property>
          <name>dfs.namenode.name.dir</name>
          <value>/home/hadoop/data/nameNode</value>
  </property>
  </configuration>"""
with open("/hadoop/etc/hadoop/hdfs-site.xml","w") as configfile:
  configfile.write(config)
config = """<configuration>
  <property>
          <name>yarn.acl.enable</name>
          <value>0</value>
  </property>

   <property>
          <name>yarn.resourcemanager.hostname</name>
          <value>node-master</value>
  </property>
  <property>
          <name>yarn.nodemanager.resource.memory-mb</name>
          <value>512</value>
  </property>

   <property>
          <name>yarn.scheduler.maximum-allocation-mb</name>
          <value>512</value>
  </property>

   <property>
          <name>yarn.scheduler.minimum-allocation-mb</name>
          <value>64</value>
  </property>

   <property>
          <name>yarn.nodemanager.vmem-check-enabled</name>
          <value>false</value>
  </property>
  </configuration>"""
with open("/hadoop/etc/hadoop/yarn-site.xml","w") as configfile:
  configfile.write(config)
java_path = subprocess.check_output(["check_java"]).decode("utf-8").split()[-1]
with open("/hadoop/etc/hadoop/hadoop-env.sh","a") as envfile:
  envfile.write("export JAVA_HOME="+java_path)
subprocess.check_output(["/usr/sbin/start_hadoop"])