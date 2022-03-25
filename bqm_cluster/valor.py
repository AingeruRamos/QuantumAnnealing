import dataManager as dtm
from dataContainer import _data_ as _dt_
import sys
import json

json_file = sys.argv[1]

result = {}
with open(json_file,) as fp:
    result = json.load(fp)

dtm.chargeData(result['problem_id'])

T = len(_dt_.inf.HT)
W = int(result['n_variables']/T)

value = 0
for i in range(result['n_variables']):
    if result['sample'][i] == 1:
        value += _dt_.inf.HT[i%T]

print(value)
totalError = 0
error = 0

for t in range(T):
    flag = 0
    for w in range(W):
        flag += result['sample'][t*W+w]
    
    if flag > 1: error += 1
print(f"R1:{error}")
totalError += error

error = 0
for w in range(W):
    for d in _dt_.inf.D:
        flag = 0
        for t in range(d[0], d[1]+1):
            flag += result['sample'][t*W+w]
        
        if flag > 1: error += 1
print(f"R2:{error}")
totalError += error

error = 0
for w in range(W):
    flag = 0
    for t in range(T):
        flag +=_dt_.inf.HT[t]*result['sample'][t*W+w]
    
    if flag > _dt_.inf.HA[w]: error += 1
print(f"R3:{error}")
totalError += error

error = 0
for w in range(W):
    for s in _dt_.inf.S:
        flag = 0
        for t in range(s[0], s[1]+1):
            flag += _dt_.inf.HT[t]*result['sample'][t*W+w]

        if flag > _dt_.inf.HS[w]: error +=1
print(f"R4:{error}")
totalError += error

error = 0
for w in range(W):
    for s in _dt_.inf.S:
        flag = 0
        for t in range(s[0], s[1]+1):
            flag += result['sample'][t*W+w]

        if flag > _dt_.inf.SW[w]: error += 1
print(f"R5:{error}")
totalError += error

error = 0
for w in range(W):
    for s in _dt_.inf.S:
        flag = 0
        for t in range(s[0], s[1]+1):
            flag += _dt_.inf.JP[t]*result['sample'][t*W+w]
        
        if flag > 1: error += 1
print(f"R6:{error}")
totalError += error

error = 0
for w in range(W):
    flag = 0
    for t in _dt_.inf.PWT[w]:
        flag += result['sample'][t*W+w]

    if flag != 0: error +=1
print(f"R7:{error}")
totalError += error

print(f"Restricciones incumplidas totales: {totalError}")

cosa = 0
jore = []
for t in range(T):
    if _dt_.inf.JP[t]:
        cosa += 1
        jore.append(_dt_.inf.HT[t])

