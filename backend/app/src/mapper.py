import csv
from opyenxes.data_in.XUniversalParser import XUniversalParser

class Mapper:
  def __init__(self):
    pass
  def mapXes(self, lfile, header):
    with open(lfile) as log_file:
      log = XUniversalParser().parse(log_file)[0]
    return log
  def mapCsv(self, lfile, header):
    mr = csv.DictReader(lfile)
    res = {}
    for row in mr:
      if header not in res:
        res[header] = [row]
      else:
        res[header].append(row)
    return res