from hadoop import HadoopInteractions

h = HadoopInteractions()
h.pushData('/src/bin/','/.')
h.getData('/.')
while True:
  pass