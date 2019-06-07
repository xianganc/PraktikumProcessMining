from hadoop import HadoopInteractions
import time

h = HadoopInteractions()
#h.pushData('/src/ubuntu/bin/','/hadoop')
h.showData('/')
while True:
  time.sleep(10)