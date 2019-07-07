import csv
from opyenxes.data_in.XUniversalParser import XUniversalParser

class Mapper:
  def __init__(self):
    pass

  def map1Xes(self, lfile, header):
    res = {}
    return res

  def map1Csv(self, lfile, activity, timestamp, case):
    res={}
    tmp = []
    with open(lfile, newline='') as f:
      reader = csv.DictReader(f)
      print(reader)
      for row in reader:
        if case in row.keys():
          print(row)
          tmp.append((row[case],row[activity],row[timestamp]))
          print(tmp)
    for entry in tmp:
      if entry[0] in res:
        res[entry[0]].append((entry[1],entry[2]))
      else:
        res[entry[0]] = [(entry[1],entry[2])]
    return res

  def map2(self):
    pass