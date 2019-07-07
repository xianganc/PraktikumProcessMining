
class Reduce:
  def __init__(self):
    pass
  def reduce1(self, logDict):
    for key in logDict.keys():
      print(sorted(logDict[key],key=lambda k:k[1]))

  def reduce2(self):
    pass