import json
import mapper
import reducer

mp = mapper.Mapper()
rp = reducer.Reduce()

tmp = mp.map1Csv('/home/ichus/Documents/PraktikumProcessMining/data/running-example.csv',activity='Activity',timestamp='time:timestamp',case='case:concept:name')
tmp = rp.reduce1(tmp)
print(rp.reduce1(tmp))