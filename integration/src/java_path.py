import subprocess

java_path = subprocess.check_output("./integration/bin/check_java").decode("utf-8").split()[-1][:-8]
subprocess.check_output(["sudo","runuser","root","-c","echo 'export JAVA_HOME=%s' >> ./hadoop/etc/hadoop/hadoop-env.sh" % java_path])