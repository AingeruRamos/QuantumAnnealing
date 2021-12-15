import dimod
import dataManager as dtm
from dataContainer import _data_ as _dt_
import constraints as cst
from qubo import setAncillaryIndexOffset, setLagrangeFactor, addToQ
import debug as dbug
import time
import dimod

print("Cargando Datos", end='')
dtm.chargeData()
setAncillaryIndexOffset(_dt_.cnt.T*_dt_.cnt.W)
setLagrangeFactor(1)
print("\rDatos Cargados")

dbug.printCNT()

print("\nGenerando Q")
bqm_gen = dimod.BQM.from_qubo({})

start_time = time.time()
"""
#Función Objetivo
print("\nFunción Objetivo")
for t in range(0, _dt_.cnt.T):
    _dt_.aux.selectedT = t
    for w in range(0, _dt_.cnt.W):
        _dt_.aux.selectedW = w
        ht = _dt_.inf.HT[_dt_.aux.selectedT]
        index = _dt_.aux.selectedT * _dt_.cnt.W + _dt_.aux.selectedW
        addToQ(Q, (index, index), -1*ht)

#Restricciones
cst.addConstraint1(bqm_gen)
cst.addConstraint2(bqm_gen)
cst.addConstraint4(bqm_gen)
cst.addConstraint5(bqm_gen)
cst.addConstraint6(bqm_gen)
"""
cst.addConstraint7(bqm_gen)

#cst.addConstraint3(bqm_gen)

total_time = time.time()-start_time

hour = total_time // 3600
rest = (total_time - 3600*hour)
min = rest // 60
rest = total_time - (3600*hour + 60*min)
seg = rest

print(f"{hour} horas, {min} minutos, {seg} segundos")