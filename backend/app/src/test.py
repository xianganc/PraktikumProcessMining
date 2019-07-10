import json
import mapper
import reducer
from alphaAlgo import Alpha
from petri import PetriNet
from subprocess import check_call

def test1():
  mp = mapper.Mapper()
  rp = reducer.Reduce()

  #tmp, tl = mp.map1Xes('/home/ichus/Documents/PraktikumProcessMining/data/roadtraffic100traces.xes',activity='concept:name',timestamp='time:timestamp',case='concept:name')
  tmp, tl = mp.map1Csv('/home/ichus/Documents/PraktikumProcessMining/data/roadtraffic100traces.csv',activity='concept:name',timestamp='time:timestamp',case='case:concept:name')
  tmp, ti, to, tl = rp.reduce1(tmp, tl)
  res = rp.reduce2(tmp, ti, to, tl)
  with open('reduced.json', "w") as reducedLog:
    json.dump(res,reducedLog)

def test2(infile):

  alpha_model = Alpha(infile)
  print('init done')
  alpha_model.generate_footprint(txtfile="{}_footprint.txt".format(infile))
  print("footprint done")
  pn = PetriNet()
  print("petrinet init done")
  pn.generate_with_alpha(alpha_model, dotfile="{}.dot".format(infile))
  print("petrinet done")
  check_call(["dot", "-Tpng", "{}.dot".format(infile),"-o", "{}.png".format(infile)])
  print("viz done")

if __name__ == '__main__':
  test1()
  print('test1 done')
  test2('reduced.json')
  print("test2 done")
