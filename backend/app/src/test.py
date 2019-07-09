import json
import mapper
import reducer
from alpha import Alpha
from petri_net import PetriNet
from subprocess import check_call

def test1():
  mp = mapper.Mapper()
  rp = reducer.Reduce()

  tmp = mp.map1Csv('/home/ichus/Documents/PraktikumProcessMining/data/running-example.csv',activity='Activity',timestamp='time:timestamp',case='case:concept:name')
  tmp = rp.reduce1(tmp)
  res = rp.reduce2(tmp)
  print(res)
  with open('reduced.json') as reducedLog:
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