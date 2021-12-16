import dataManager as dtm
from dataContainer import _data_ as _dt_
import problem as prb
from qubo import setAncillaryIndexOffset, setLagrangeFactor
import saveManager as svm
import debug as dbug
import time

print("Cargando Datos", end='')
dtm.chargeData()
setAncillaryIndexOffset(_dt_.cnt.T*_dt_.cnt.W)
setLagrangeFactor(1)
print("\rDatos Cargados")

dbug.printCNT()

print("\nGenerando Q")

start_time = time.time()

#Función Objetivo
Q = prb.createObjetiveFunction()

#Restricciones
prb.addConstraint1(Q)
prb.addConstraint2(Q)
prb.addConstraint4(Q)
prb.addConstraint5(Q)
prb.addConstraint6(Q)
prb.addConstraint7(Q)

svm.saveQ(Q)
Q = {}

#prb.addConstraint3(Q)


svm.makeUnion()

total_time = time.time()-start_time

hour = total_time // 3600
rest = (total_time - 3600*hour)
min = rest // 60
rest = total_time - (3600*hour + 60*min)
seg = rest

print(f"{hour} horas, {min} minutos, {seg} segundos")