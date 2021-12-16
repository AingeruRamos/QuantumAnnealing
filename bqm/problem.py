from dataContainer import _data_
from constraints import cst_list
from qubo import qubo, addToQ
import debug as dbug

def createObjetiveFunction():
    Q = {}

    for t in range(0, _data_.cnt.T):
        _data_.aux.selectedT = t
        for w in range(0, _data_.cnt.W):
            _data_.aux.selectedW = w
            ht = _data_.inf.HT[_data_.aux.selectedT]
            index = _data_.aux.selectedT * _data_.cnt.W + _data_.aux.selectedW
            addToQ(Q, (index, index), -1*ht)

    return Q

def addConstraint1(Q):

    dbug.setAuxInfo(_data_.cnt.T, 1)
    for t in range(_data_.cnt.T):
        _data_.aux.selectedT = t
        dbug.printAuxInfo()
        qubo(Q, cst_list[0])

def addConstraint2(Q):

    dbug.setAuxInfo(_data_.cnt.D * _data_.cnt.W, 2)
    for d in range(_data_.cnt.D):
        _data_.aux.selectedD = d
        for w in range(_data_.cnt.W):
            _data_.aux.selectedW = w
            dbug.printAuxInfo()
            qubo(Q, cst_list[1])

def addConstraint3(Q):

    dbug.setAuxInfo(_data_.cnt.W, 3)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        dbug.printAuxInfo()
        qubo(Q, cst_list[2])

def addConstraint4(Q):

    dbug.setAuxInfo(_data_.cnt.W * _data_.cnt.S, 4)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        for s in range(_data_.cnt.S):
            _data_.aux.selectedS = s
            dbug.printAuxInfo()
            qubo(Q, cst_list[3])

def addConstraint5(Q):

    dbug.setAuxInfo(_data_.cnt.W * _data_.cnt.S, 5)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        for s in range(_data_.cnt.S):
            _data_.aux.selectedS = s
            dbug.printAuxInfo()
            qubo(Q, cst_list[4])

def addConstraint6(Q):

    dbug.setAuxInfo(_data_.cnt.W * _data_.cnt.S, 6)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        for s in range(_data_.cnt.S):
            _data_.aux.selectedS = s
            dbug.printAuxInfo()
            qubo(Q, cst_list[5])

def addConstraint7(Q):

    dbug.setAuxInfo(_data_.cnt.W, 7)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        dbug.printAuxInfo()
        qubo(Q, cst_list[6])
