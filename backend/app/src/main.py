from hadoop import HadoopInteractions
import time
import os

h = HadoopInteractions()
h.pushData('/src/bin/','/hadoop')
h.showData('/')
while True:
  for (dirpath, dirnames, filenames) in os.walk("/data"):
    for element in filenames:
      print(os.sep.join([dirpath,filenames]))
      h.pushData(os.sep.join([dirpath,filenames]),"/hadoop"+dirpath)
    for element in dirnames:
      print(os.sep.join([dirpath,dirnames]))
      h.pushData(os.sep.join([dirpath,dirnames]),"/hadoop"+dirpath)
  time.sleep(60)
