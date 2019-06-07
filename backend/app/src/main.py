from hadoop import HadoopInteractions
import time

h = HadoopInteractions()
h.pushData('/src/bin/','/.')
h.showData('/.')
while True:
  time.sleep(10)