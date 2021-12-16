from dataContainer import _data_
from constraints import cst_list
from qubo import qubo
import debug as dbug
import dimod

def createObjetiveFunction():
    bqm = dimod.BQM.from_qubo({})

    for t in range(0, _data_.cnt.T):
        _data_.aux.selectedT = t
        for w in range(0, _data_.cnt.W):
            _data_.aux.selectedW = w
            ht = _data_.inf.HT[_data_.aux.selectedT]
            index = _data_.aux.selectedT * _data_.cnt.W + _data_.aux.selectedW
            bqm.add_linear(index, -1*ht)

    return bqm

def addConstraint1(bqm):
    bqm_c = dimod.BQM.from_qubo({})

    dbug.setAuxInfo(_data_.cnt.T, 1)
    for t in range(_data_.cnt.T):
        _data_.aux.selectedT = t
        dbug.printAuxInfo()
        qubo(bqm, cst_list[0])

    #bqm_c.scale(1.5)
    bqm.update(bqm_c)

def addConstraint2(bqm):
    bqm_c = dimod.BQM.from_qubo({})

    dbug.setAuxInfo(_data_.cnt.D * _data_.cnt.W, 2)
    for d in range(_data_.cnt.D):
        _data_.aux.selectedD = d
        for w in range(_data_.cnt.W):
            _data_.aux.selectedW = w
            dbug.printAuxInfo()
            qubo(bqm, cst_list[1])

    #bqm_c.scale(1.5)
    bqm.update(bqm_c)

def addConstraint3(bqm):
    bqm_c = dimod.BQM.from_qubo({})

    dbug.setAuxInfo(_data_.cnt.W, 3)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        dbug.printAuxInfo()
        qubo(bqm, cst_list[2])
        #bqm_c.scale(1.5)
        bqm.update(bqm_c)

def addConstraint4(bqm):
    bqm_c = dimod.BQM.from_qubo({})

    dbug.setAuxInfo(_data_.cnt.W * _data_.cnt.S, 4)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        for s in range(_data_.cnt.S):
            _data_.aux.selectedS = s
            dbug.printAuxInfo()
            qubo(bqm, cst_list[3])

    #bqm_c.scale(1.5)
    bqm.update(bqm_c)

def addConstraint5(bqm):
    bqm_c = dimod.BQM.from_qubo({})

    dbug.setAuxInfo(_data_.cnt.W * _data_.cnt.S, 5)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        for s in range(_data_.cnt.S):
            _data_.aux.selectedS = s
            dbug.printAuxInfo()
            qubo(bqm, cst_list[4])

    #bqm_c.scale(1.5)
    bqm.update(bqm_c)

def addConstraint6(bqm):
    bqm_c = dimod.BQM.from_qubo({})

    dbug.setAuxInfo(_data_.cnt.W * _data_.cnt.S, 6)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        for s in range(_data_.cnt.S):
            _data_.aux.selectedS = s
            dbug.printAuxInfo()
            qubo(bqm, cst_list[5])

    #bqm_c.scale(1.5)
    bqm.update(bqm_c)

def addConstraint7(bqm):
    bqm_c = dimod.BQM.from_qubo({})

    dbug.setAuxInfo(_data_.cnt.W, 7)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        dbug.printAuxInfo()
        qubo(bqm, cst_list[6])
        #bqm_c.scale(1.5)
        bqm.update(bqm_c)
