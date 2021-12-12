import dataManager as dtm
from dataContainer import _data_ as _dt_
from constraints import createCST, cst_list
from qubo import qubo, setAncillaryIndexOffset, setLagrangeFactor
import saveManager as svm
import debug as dbug
import time
#from dwave.system import DWaveSampler, EmbeddingComposite

print("Cargando Datos", end='')
dtm.chargeData()
createCST()
setAncillaryIndexOffset(_dt_.cnt.T*_dt_.cnt.W)
setLagrangeFactor(1)
print("\rDatos Cargados")

dbug.printCNT()

print("\nGenerando Q")
Q = {}

start_time = time.time()
"""
#Función Objetivo
print("\nFunción Objetivo")
for t in range(0, _dt_.cnt.T):
    _dt_.aux.selectedT = t
    for w in range(0, _dt_.cnt.W):
        _dt_.aux.selectedW = w
        ht = _dt_.inf.H[_dt_.aux.selectedT]
        index = _dt_.aux.selectedT * _dt_.cnt.W + _dt_.aux.selectedW
        Q[(index, index)] = -1*ht

#Guardar esto de alguna forma
"""

#Restriccion 1
dbug.setAuxInfo(_dt_.cnt.T, 1)
for t in range(_dt_.cnt.T):
    _dt_.aux.selectedT = t
    dbug.printAuxInfo()
    qubo(Q, cst_list[0])

dtm.restartAux()

#Restriccion 2
dbug.setAuxInfo(_dt_.cnt.D * _dt_.cnt.W, 2)
for d in range(_dt_.cnt.D):
    _dt_.aux.selectedD = d
    for w in range(_dt_.cnt.W):
        _dt_.aux.selectedW = w
        dbug.printAuxInfo()
        qubo(Q, cst_list[1])

dtm.restartAux()

#Restriccion 4
dbug.setAuxInfo(_dt_.cnt.W * _dt_.cnt.S, 4)
for w in range(_dt_.cnt.W):
    _dt_.aux.selectedW = w
    for s in range(_dt_.cnt.S):
        _dt_.aux.selectedS = s
        dbug.printAuxInfo()
        qubo(Q, cst_list[3])

dtm.restartAux()

#Restriccion 5
dbug.setAuxInfo(_dt_.cnt.W * _dt_.cnt.S, 5)
for w in range(_dt_.cnt.W):
    _dt_.aux.selectedW = w
    for s in range(_dt_.cnt.S):
        _dt_.aux.selectedS = s
        dbug.printAuxInfo()
        qubo(Q, cst_list[4])

dtm.restartAux()

#Restriccion 6
dbug.setAuxInfo(_dt_.cnt.W * _dt_.cnt.S, 6)
for w in range(_dt_.cnt.W):
    _dt_.aux.selectedW = w
    for s in range(_dt_.cnt.S):
        _dt_.aux.selectedS = s
        dbug.printAuxInfo()
        qubo(Q, cst_list[5])

dtm.restartAux()

#Restriccion 7
dbug.setAuxInfo(_dt_.cnt.P * _dt_.cnt.W, 7)
for p in range(_dt_.cnt.P):
    _dt_.aux.selectedP = p
    for w in range(_dt_.cnt.W):
        _dt_.aux.selectedW = w
        dbug.printAuxInfo()
        qubo(Q, cst_list[6])

dtm.restartAux()

svm.saveQ(Q)
Q = {}

#Restriccion 3
counter = 1
dbug.setAuxInfo(_dt_.cnt.W, 3)
for w in range(_dt_.cnt.W):
    _dt_.aux.selectedW = w
    dbug.printAuxInfo()
    qubo(Q, cst_list[2])
    if counter == 7:
        print()
        counter = 0
        svm.saveQ(Q)
        Q = {}
    counter += 1

if counter != 1:
    svm.saveQ(Q)
    Q = {}

svm.makeUnion()

total_time = time.time()-start_time

hour = total_time // 3600
rest = (total_time - 3600*hour)
min = rest // 60
rest = total_time - (3600*hour + 60*min)
seg = rest

print(f"{hour} horas, {min} minutos, {seg} segundos")

#sampler = EmbeddingComposite(DWaveSampler())
#sampleset = sampler.sample.qubo(Q, num_reads=10, chain_strength=10)
#print(sampleset)