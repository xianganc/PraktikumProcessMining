import json

class Reduce:
  def __init__(self):
    pass

def reduce1(self, logDict):
    resDict = {}
    tmp = {}
    for key in logDict.keys():
      trace = sorted(logDict[key],key=lambda k:k[1])
      for i in range(len(trace)):
        for j in range(len(trace)):
          if i == j:
            continue
          elif i < j:
            if (trace[j][0],trace[i][0]) not in tmp:
              tmp[(trace[j][0],trace[i][0])] = (False,False)
            tmp[(trace[j][0],trace[i][0])] = (False or tmp[(trace[j][0],trace[i][0])][0],tmp[(trace[j][0],trace[i][0])][1] or True)
          else:
            if (trace[j][0],trace[i][0]) not in tmp:
              tmp[(trace[j][0],trace[i][0])] = (False,False)
            tmp[(trace[j][0],trace[i][0])] = (True or tmp[(trace[j][0],trace[i][0])][0],tmp[(trace[j][0],trace[i][0])][1] or False)
    return tmp

  def reduce2(self):
    pass
