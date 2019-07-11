import csv
import json
import os
from pm4py.objects.log.importer.xes import factory as xes_importer


class Mapper:
  def __init__(self):
    pass

  def map1Xes(self, lfile, activity="concept:name", timestamp="time:timestamp", case="concept:name"):
    tmp = [ ]
    res = {}
    tl = set()
    log = xes_importer.import_log(lfile)
    for trace in log:
      for event in trace:
        tmp.append((trace.attributes[case],event[activity],event[timestamp]))
        tl.add(event[activity])
    for entry in tmp:
      if entry[0] in res:
        res[entry[0]].append((entry[1],entry[2]))
      else:
        res[entry[0]] = [(entry[1],entry[2])]
      tl.add(entry[1])
    return res, tl

  def map1Csv(self, lfile, activity="concept:name", timestamp="time:timestamp", case="case:concept:name"):
    res={}
    tmp = []
    tl = set()
    with open(lfile, newline='') as f:
      reader = csv.DictReader(f)
      for row in reader:
        if case in row.keys():
          tmp.append((row[case],row[activity],row[timestamp]))
          tl.add(row[activity])
    for entry in tmp:
      if entry[0] in res:
        res[entry[0]].append((entry[1],entry[2]))
      else:
        res[entry[0]] = [(entry[1],entry[2])]
    return res, tl
