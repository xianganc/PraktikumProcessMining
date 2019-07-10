import csv
import json
import os
from pm4py.objects.log.importer.xes import factory as xes_importer


class Mapper:
  def __init__(self):
    pass

  def map1Xes(self, lfile, activity, timestamp, case):
    tmp = [ ]
    res = {}
    log = xes_importer.import_log(lfile)
    for trace in log:
      for event in trace:
        if case in trace.attributes:
          tmp.append((trace.attributes[case],event[activity],event[timestamp]))
    tl = set()
    for entry in tmp:
      if entry[0] in res:
        res[entry[0]].append((entry[1],entry[2]))
      else:
        res[entry[0]] = [(entry[1],entry[2])]
      tl.add(entry[1])
    return res, tl

  def map1Csv(self, lfile, activity, timestamp, case):
    res={}
    tmp = []
    with open(lfile, newline='') as f:
      reader = csv.DictReader(f)
      for row in reader:
        if case in row.keys():
          tmp.append((row[case],row[activity],row[timestamp]))
    tl = set()
    for entry in tmp:
      if entry[0] in res:
        res[entry[0]].append((entry[1],entry[2]))
      else:
        res[entry[0]] = [(entry[1],entry[2])]
      tl.add(entry[1])
    return res, tl
