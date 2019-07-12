import itertools
import copy
import time
import json
import sys
import subprocess
import shutil
from petri import PetriNet

class Alpha():
  def __init__(self, reducedDict):
    with open(reducedDict) as inf:
      jsoned = json.load(inf)
    self.pr = set()
    self.ds = set()
    self.cs = set()
    for element in jsoned.keys():
      if element == 'ti':
        self.ti = set(jsoned[element])
      elif element == 'to':
        self.to = set(jsoned[element])
      elif element == 'tl':
        self.tl = set(jsoned[element])
      elif element == 'pr':
        for entry in jsoned[element]:
          self.pr.add(tuple(entry))
      elif element == 'cs':
        for entry in jsoned[element]:
          self.cs.add(tuple(entry))
      elif element == 'ds':
        for entry in jsoned[element]:
          self.ds.add(tuple(entry))
    self.ind = self.choice(self.tl, self.cs, self.pr)
    print("read log done")
    print("these sets")
    self.xl = self.get_XL_set(self.tl, self.ind, self.cs)
    print("xl set")
    self.yl = self.get_YL_set(self.xl, self.pr)
    print("yl set")
    print("init done")


  def __str__(self):
    alpha_sets = []
    alpha_sets.append("TI set: {}".format(self.ti))
    alpha_sets.append("TO set: {}".format(self.to))
    alpha_sets.append("XL set: {}".format(self.xl))
    alpha_sets.append("YL set: {}".format(self.yl))
    return '\n'.join(alpha_sets)

  def get_XL_set(self, tl, ind, cs):
    xl = set()
    subsets = itertools.chain.from_iterable(itertools.combinations(tl, r) for r in range(1, len(tl) + 1))
    independent_a_or_b = [a_or_b for a_or_b in subsets if self.__is_ind_set(a_or_b, ind)]
    for a,b in itertools.product(independent_a_or_b, independent_a_or_b):
      if self.__is_cs_set((a,b), cs):
        xl.add((a,b))
    print(xl)
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

  def choice(self, tl, cs, pr):
    ind = set()
    all_permutations = itertools.permutations(tl, 2)
    for pair in all_permutations:
      if pair not in cs and pair[::-1] not in cs and pair not in pr:
        ind.add(pair)
    return ind

if __name__ == '__main__':
  infile = sys.argv[1]
  alpha_model = Alpha(infile)
  print('init done')
  alpha_model.generate_footprint(txtfile="{}_footprint.txt".format(infile))
  print("footprint done")
  pn = PetriNet()
  print("petrinet init done")
  pn.generate_with_alpha(alpha_model, dotfile="{}.dot".format(infile))
  print("petrinet done")
  subprocess.check_call(["dot", "-Tpng", "{}.dot".format(infile),"-o", "{}.png".format('output')])
  shutil.move('output.png', '/data/output.png')
  print("viz done")
