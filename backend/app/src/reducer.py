
class Reduce:
  def __init__(self):
    pass
  def reduce1(self, logDict):
    resDict = {}
    tmp = set()
    for key in logDict.keys():
      trace = sorted(logDict[key],key=lambda k:k[1])
      for i in trace:
        for j in trace:
          if i == j:
            continue
          tmp.add(((trace[i],trace[j]),True))
    print(tmp)
  def reduce2(self):
    pass