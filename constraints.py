from dataContainer import _data_
import debug as dbug
from qubo import qubo
import dimod

class CST:
    def __init__(self, alpha_f, m_f, d_f, i_f):
        self.alpha_f = alpha_f
        self.m_f = m_f
        self.d_f = d_f
        self.i_f = i_f

#########################
def indexQBitW(w):
    return _data_.aux.selectedT * _data_.cnt.W + w

def indexQBitT(t):
    return t * _data_.cnt.W + _data_.aux.selectedW
#########################
def alpha_1():
    return range(_data_.cnt.W)

def m_1(w):
    return 1

def d_1():
    return 1
#########################
def alpha_2():
    t_interval_start, t_interval_end = _data_.inf.D[_data_.aux.selectedD]
    return range(t_interval_start, t_interval_end+1)

def m_2(t):
    return 1

def d_2():
    return 1
#########################
def alpha_3():
    return range(_data_.cnt.T)

def m_3(t):
    return _data_.inf.HT[t]

def d_3():
    return _data_.inf.HA[_data_.aux.selectedW]
#########################
def alpha_4():
    t_interval_start, t_interval_end = _data_.inf.S[_data_.aux.selectedS]
    return range(t_interval_start, t_interval_end+1)

def m_4(t):
    return _data_.inf.HT[t]

def d_4():
    return _data_.inf.HS[_data_.aux.selectedW]
#########################
def alpha_5():
    t_interval_start, t_interval_end = _data_.inf.S[_data_.aux.selectedS]
    return range(t_interval_start, t_interval_end+1)

def m_5(t):
    return 1

def d_5():
    return _data_.inf.SW[_data_.aux.selectedW]
#########################
def alpha_6():
    t_interval_start, t_interval_end = _data_.inf.S[_data_.aux.selectedS]
    return range(t_interval_start, t_interval_end+1)

def m_6(t):
    return _data_.inf.JP[t]

def d_6():
    return 1
#########################
def alpha_7():
    return _data_.inf.PWT[_data_.aux.selectedW]

def m_7(t):
    return 1

def d_7():
    return 0
#########################

def addConstraint1(bqm):
    Q = {}
    cst = CST(alpha_1, m_1, d_1, indexQBitW)

    dbug.setAuxInfo(_data_.cnt.T, 1)
    for t in range(_data_.cnt.T):
        _data_.aux.selectedT = t
        dbug.printAuxInfo()
        qubo(Q, cst)

    bqm_c = dimod.BQM.from_qubo(Q)
    #bqm_c.scale(1.5)
    bqm.update(bqm_c)

def addConstraint2(bqm):
    Q = {}
    cst = CST(alpha_2, m_2, d_2, indexQBitT)

    dbug.setAuxInfo(_data_.cnt.D * _data_.cnt.W, 2)
    for d in range(_data_.cnt.D):
        _data_.aux.selectedD = d
        for w in range(_data_.cnt.W):
            _data_.aux.selectedW = w
            dbug.printAuxInfo()
            qubo(Q, cst)

    bqm_c = dimod.BQM.from_qubo(Q)
    #bqm_c.scale(1.5)
    bqm.update(bqm_c)

def addConstraint3(bqm):
    Q = {}
    cst = CST(alpha_3, m_3, d_3, indexQBitT)

    dbug.setAuxInfo(_data_.cnt.W, 3)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        dbug.printAuxInfo()
        qubo(Q, cst)
        bqm_c = dimod.BQM.from_qubo(Q)
        #bqm_c.scale(1.5)
        bqm.update(bqm_c)
        Q = {}

def addConstraint4(bqm):
    Q = {}
    cst = CST(alpha_4, m_4, d_4, indexQBitT)

    dbug.setAuxInfo(_data_.cnt.W * _data_.cnt.S, 4)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        for s in range(_data_.cnt.S):
            _data_.aux.selectedS = s
            dbug.printAuxInfo()
            qubo(Q, cst)

    bqm_c = dimod.BQM.from_qubo(Q)
    #bqm_c.scale(1.5)
    bqm.update(bqm_c)

def addConstraint5(bqm):
    Q = {}
    cst = CST(alpha_5, m_5, d_5, indexQBitT)

    dbug.setAuxInfo(_data_.cnt.W * _data_.cnt.S, 5)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        for s in range(_data_.cnt.S):
            _data_.aux.selectedS = s
            dbug.printAuxInfo()
            qubo(Q, cst)

    bqm_c = dimod.BQM.from_qubo(Q)
    #bqm_c.scale(1.5)
    bqm.update(bqm_c)

def addConstraint6(bqm):
    Q = {}
    cst = CST(alpha_6, m_6, d_6, indexQBitT)

    dbug.setAuxInfo(_data_.cnt.W * _data_.cnt.S, 6)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        for s in range(_data_.cnt.S):
            _data_.aux.selectedS = s
            dbug.printAuxInfo()
            qubo(Q, cst)

    bqm_c = dimod.BQM.from_qubo(Q)
    #bqm_c.scale(1.5)
    bqm.update(bqm_c)

def addConstraint7(bqm):
    Q = {}
    cst = CST(alpha_7, m_7, d_7, indexQBitT)

    dbug.setAuxInfo(_data_.cnt.W, 7)
    for w in range(_data_.cnt.W):
        _data_.aux.selectedW = w
        dbug.printAuxInfo()
        qubo(Q, cst)
        bqm_c = dimod.BQM.from_qubo(Q)
        #bqm_c.scale(1.5)
        bqm.update(bqm_c)
        Q = {}
