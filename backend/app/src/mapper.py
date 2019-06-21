import csv
from opyenxes.data_in.XUniversalParser import XUniversalParser

class Mapper:
  def __init__(self, fileExtention, key):
    pass
  def mapXes(self, lfile, header):
    with open(lfile) as log_file:
      log = XUniversalParser().parse(log_file)[0]
    return log
  def mapCsv(self, lfile, header):
    mr = csv.DictReader(lfile)
    res = []
    for row in mr:
      res.append(row[header])
    return res