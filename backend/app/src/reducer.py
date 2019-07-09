import json

class Reduce:
  def __init__(self):
    pass

  def reduce1(self, logDict):
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

  def reduce2(self, reducedDict):
    res = {}
    res['ds'] = set()
    res['cs'] = set()
    res['pr'] = set()
    res['ind'] = set()
    res['tl'] = set()
    for element in reducedDict.keys():
      if reducedDict[element][0]:
        res['ds'].add(element)
      if reducedDict[element] == (True, False):
        res['cs'].add(element)
      if reducedDict[element] == (True, True):
        res['pr'].add(element)
      if reducedDict[element] == (False, False):
        res['ind'].add(element)
      res['tl'].add(element)
    return res
