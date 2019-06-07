import subprocess

class HadoopInteractions:
  def __init__(self):
    """creating Interface"""
    pass

  def pushData(self,from_,to_):
    """ pushing data into hadoop """
    subprocess.check_output(["runuser","hadoop","-c" ,'/src/bin/hdfs -mkdir '+ to_])
    subprocess.check_output(["runuser","hadoop","-c" ,'/src/bin/hdfs -put '+from_ + ' '+ to_])
    pass

  def getData(self, from_, to_):
    """ get data from hadoop """
    subprocess.check_output(["runuser","hadoop","-c" ,'/src/bin/hdfs -get '+ from_ + ' '+ to_])
    pass

  def showData(self,from_):
    """ get data from hadoop """
    subprocess.check_output(["runuser","hadoop","-c" ,'/src/bin/hdfs -ls -R '+ from_])
    pass

  def runMR(self, data):
    """ running the Map-Reduce Job """
    pass

  def runAlpha(self, data):
    """ running the alpha-algorithm """
    pass

