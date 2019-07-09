import itertools
import copy
import time

class Alpha():
  def __init__(self, reducedDict):
    self.start = [time.time()]
    print("start init")
    self.log = reducedDict
    self.tl = self.log['tl']
    self.ds = self.log['ds']
    self.cs = self.log['cs']
    self.pr = self.log['pr']
    self.ind = self.log['ind']
    print("read log done")
    #self.ti = self.get_TI_set()
    #self.to = self.get_TO_set()
    print("these sets")
    self.xl = self.get_XL_set(self.tl, self.ind, self.cs)
    print("xl set")
    self.yl = self.get_YL_set(self.xl, self.pr)
    print("init done")


  def __str__(self):
    alpha_sets = []
    #alpha_sets.append("TI set: {}".format(self.ti))
    #alpha_sets.append("TO set: {}".format(self.to))
    alpha_sets.append("XL set: {}".format(self.xl))
    alpha_sets.append("YL set: {}".format(self.yl))
    return '\n'.join(alpha_sets)

  def get_TL_set(self):
    tl = set()
    for item in self.log:
      for i in item:
        tl.add(i)
    return tl

  def get_TI_set(self):
    ti = set()
    for item in self.log:
      ti.add(item[0])
    return ti

  def get_TO_set(self):
    to = set()
    for item in self.log:
      to.add(item[-1])
    return to

  def get_XL_set(self, tl, ind, cs):
    xl = set()
    subsets = itertools.chain.from_iterable(itertools.combinations(tl, r) for r in range(1, len(tl) + 1))
    self.start.append(time.time())
    independent_a_or_b = [a_or_b for a_or_b in subsets if self.__is_ind_set(a_or_b, ind)]
    self.start.append(time.time())
    print(str(self.start[-1]-self.start[-2]) + " seconds")
    print("after inde")
    for a, b in itertools.product(independent_a_or_b, independent_a_or_b):
      print(a,b)
      if self.__is_cs_set((a, b), cs):
        xl.add((a, b))
    return xl

  def __is_ind_set(self, s, ind):
    if len(s) == 1:
      return True
    else:
      s_all = itertools.combinations(s, 2)
      for pair in s_all:
        if pair not in ind:
         return False
      return True

  def __is_cs_set(self, s, cs):
    set_a, set_b = s[0], s[1]
    s_all = itertools.product(set_a, set_b)
    for pair in s_all:
      if pair not in cs:
        return False
    return True

  def get_YL_set(self, xl, pr):
    yl = copy.deepcopy(xl)
    s_all = itertools.combinations(yl, 2)
    for pair in s_all:
      if self.__issubset(pair[0], pair[1]):
        yl.discard(pair[0])
      elif self.__issubset(pair[1], pair[0]):
        yl.discard(pair[1])
    self_loop = set()
    for pair in pr:
      if pair == pair[::-1]:
        self_loop.add(pair[0])
    to_be_deleted = set()
    for pair in yl:
      if self.__contains(pair, self_loop):
        to_be_deleted.add(pair)
    for pair in to_be_deleted:
      yl.discard(pair)
    return yl

  def __issubset(self, a, b):
    if set(a[0]).issubset(b[0]) and set(a[1]).issubset(b[1]):
      return True
    return False

  def __contains(self, a, b):
      return any(j == i[0] for i in a for j in b)

  def get_footprint(self):
    footprint = []
    footprint.append("All transitions: {}".format(self.tl))
    footprint.append("Direct succession: {}".format(self.ds))
    footprint.append("Causality: {}".format(self.cs))
    footprint.append("Parallel: {}".format(self.pr))
    footprint.append("Choice: {}".format(self.ind))
    return '\n'.join(footprint)

  def generate_footprint(self, txtfile='footprint.txt'):
    with open(txtfile, 'w') as f:
      f.write(self.get_footprint())
