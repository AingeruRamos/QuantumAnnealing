import dimod
import dataManager as dtm
from dataContainer import _data_ as _dt_
import problem as prb
from qubo import setAncillaryIndexOffset, setLagrangeFactor
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
bqm_gen = prb.createObjetiveFunction()

#Restricciones
prb.addConstraint1(bqm_gen)
prb.addConstraint2(bqm_gen)
prb.addConstraint4(bqm_gen)
prb.addConstraint5(bqm_gen)
prb.addConstraint6(bqm_gen)

#prb.addConstraint7(bqm_gen)

#prb.addConstraint3(bqm_gen)

total_time = time.time()-start_time

hour = total_time // 3600
rest = (total_time - 3600*hour)
min = rest // 60
rest = total_time - (3600*hour + 60*min)
seg = rest

print(f"{hour} horas, {min} minutos, {seg} segundos")