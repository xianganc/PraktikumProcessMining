import json
import mapper
mp = mapper.Mapper()
print(json.dumps(mp.map1Csv('/home/ichus/Documents/PraktikumProcessMining/data/running-example.csv',activity='Activity',timestamp='time:timestamp',case='case:concept:name'),indent=2))
