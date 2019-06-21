import subprocess
import os

class HadoopInteractions:
  def __init__(self):
    """creating Interface"""
    pass

  def data(self):
    """ """
    for (dirpath, dirnames, filenames) in os.walk('/data'):
      self.pushData(os.path.join(dirpath+filenames),'/')

  def pushData(self,from_,to_):
    """ pushing data into hadoop """
    subprocess.check_output(["/src/bin/hdfs","dfs","-mkdir","-p","/home"+to_])
    subprocess.check_output(["/src/bin/hdfs","dfs","-put",from_,"/home"+to_])
    subprocess.check_output(["rm", "-f",from_])
    pass

  def getData(self, from_, to_):
    """ get data from hadoop """
    subprocess.check_output(["/src/bin/hdfs", "dfs", "-get", from_,"/home"+to_])
    pass

  def showData(self,from_):
    """ get data from hadoop """
    out = subprocess.check_output(["/src/bin/hdfs", "dfs", "-ls", "-R", "/home"+from_])
    res = []
    out = out.decode('utf-8').splitlines()
    for line in out:
      res.append(line.split()[-1])
    return res