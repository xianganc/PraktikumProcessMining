import json
import itertools

class Reduce:
  def __init__(self):
    pass

  def reduce1(self, logDict, tl):
    tmp = {}
    ti = set()
    to = set()
    for a,b in itertools.product(tl,tl):
      if (b,a) in tmp:
        continue
      tmp[(a,b)] = (False,False)
    for key in logDict.keys():
      trace = sorted(logDict[key],key=lambda k:k[1])
      for i in range(len(trace)):
        if i == 0:
          ti.add(trace[i][0])
        if i == len(trace)-1:
          to.add(trace[i][0])
        for j in range(len(trace)):
          if i == j:
            continue
          elif i+1 == j:
            if (trace[j][0],trace[i][0]) not in tmp:
              tmp[(trace[j][0],trace[i][0])] = (False,False)
            tmp[(trace[j][0],trace[i][0])] = (False or tmp[(trace[j][0],trace[i][0])][0],tmp[(trace[j][0],trace[i][0])][1] or True)
          elif i == j+1:
            if (trace[j][0],trace[i][0]) not in tmp:
              tmp[(trace[j][0],trace[i][0])] = (False,False)
            tmp[(trace[j][0],trace[i][0])] = (True or tmp[(trace[j][0],trace[i][0])][0],tmp[(trace[j][0],trace[i][0])][1] or False)
    return tmp, ti, to, tl

  def reduce2(self, reducedDict, ti, to, tl):
    res = {}
    res['ds'] = set()
    res['cs'] = set()
    res['pr'] = set()
    res['ind'] = set()
    res['tl'] = list(tl)
    for element in reducedDict.keys():
      if reducedDict[element][0]:
        res['ds'].add(element)
      if reducedDict[element] == (True, False):
        res['cs'].add(element)
      if reducedDict[element] == (True, True):
        res['pr'].add(element)
      if reducedDict[element] == (False, False):
        res['ind'].add(element)
    for element in res:
        res[element] = list(res[element])
    res['ti'] = list(ti)
    res['to'] = list(to)
    return res
