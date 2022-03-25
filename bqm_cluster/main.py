import dataManager as dtm
from dataContainer import _data_ as _dt_
import problem as prb
from qubo import getAncillaryIndexOffset, setAncillaryIndexOffset, setLagrangeFactor
import debug as dbug
import tools as tls
import time
import sys
import dimod
from dwave.cloud import Client
import json

problem_id = sys.argv[1]
qpu_exec_time = int(sys.argv[2])
lf = 1

dtm.chargeData(problem_id)
setAncillaryIndexOffset(_dt_.cnt.T*_dt_.cnt.W)
setLagrangeFactor(lf)
print("Datos Cargados")

dbug.printCNT()

print("\nGenerando Q")
start_time = time.time()

result = {}
result['problem_id'] = problem_id
result['n_variables'] = getAncillaryIndexOffset()
result['qpu_time'] = qpu_exec_time

#Función Objetivo
bqm_gen = prb.createObjetiveFunction()

#Restricciones

prb.addConstraint1(bqm_gen, 100)
print('Restriccion 1: OK')
tls.printRAMUsage()

prb.addConstraint2(bqm_gen, 100)
print('Restriccion 2: OK')
tls.printRAMUsage()

prb.addConstraint4(bqm_gen, 100)
print('Restriccion 4: OK')
tls.printRAMUsage()

prb.addConstraint5(bqm_gen, 100)
print('Restriccion 5: OK')
tls.printRAMUsage()
'''
prb.addConstraint6(bqm_gen, 100)
print('Restriccion 6: OK')
tls.printRAMUsage()
'''
prb.addConstraint7(bqm_gen, 100)
print('Restriccion 7: OK')
tls.printRAMUsage()

prb.addConstraint3(bqm_gen, 100)
print('Restriccion 3: OK')
tls.printRAMUsage()

print('Q generado')

result['n_cubits'] = getAncillaryIndexOffset()

client = Client.from_config(config_file='./dwave.conf')

solver_list = client.get_solvers(hybrid=True)
solver_id = solver_list[0].id
solver = client.get_solver(name=solver_id)

print('Usando QPU')

samples = solver.sample_bqm(bqm_gen, time_limit=qpu_exec_time)
samples.wait()

print('Resultados recibidos')
print(f"Resultados escritos en json/{problem_id}_{qpu_exec_time}_{lf}.json")

result['sample'] = []
for v in samples.samples[0]:
    result['sample'].append(int(v))

fp = open(f"json/{problem_id}_{qpu_exec_time}_{lf}.json", 'w')
print(json.JSONEncoder().encode(result), file=fp)
fp.close()

client.close()

total_time = time.time()-start_time

hour = total_time // 3600
rest = (total_time - 3600*hour)
min = rest // 60
rest = total_time - (3600*hour + 60*min)
seg = rest

print(f"{int(hour)} horas, {int(min)} minutos, {int(seg)} segundos")
