from dataContainer import _data_

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
    return [0, _data_.cnt.W]

def m_1(w):
    return 1

def d_1():
    return 1
#########################
def alpha_2():
    t_interval = _data_.inf.D[_data_.aux.selectedD]
    return [t_interval[0], t_interval[1]+1]

def m_2(t):
    return 1

def d_2():
    return 1
#########################
def alpha_3():
    return [0, _data_.cnt.T]

def m_3(t):
    return _data_.inf.HT[t]

def d_3():
    return _data_.inf.HA[_data_.aux.selectedW]
#########################
def alpha_4():
    t_interval = _data_.inf.S[_data_.aux.selectedS]
    return [t_interval[0], t_interval[1]+1]

def m_4(t):
    return _data_.inf.HT[t]

def d_4():
    return _data_.inf.HS[_data_.aux.selectedW]
#########################
def alpha_5():
    t_interval = _data_.inf.S[_data_.aux.selectedS]
    return [t_interval[0], t_interval[1]+1]

def m_5(t):
    return 1

def d_5():
    return _data_.inf.SW[_data_.aux.selectedW]
#########################
def alpha_6():
    t_interval = _data_.inf.S[_data_.aux.selectedS]
    return [t_interval[0], t_interval[1]+1]

def m_6(t):
    return _data_.inf.JP[t]

def d_6():
    return 1
#########################
def alpha_7():
    return [0, _data_.cnt.T]

def m_7(t):
    p = _data_.aux.PArray[_data_.aux.selectedP]
    if p in _data_.inf.PT[t]:
        if p in _data_.inf.PW[_data_.aux.selectedW]:
            return 1
    return 0

def d_7():
    d = 0
    p = _data_.aux.PArray[_data_.aux.selectedP]
    if p in _data_.inf.PW[_data_.aux.selectedW]:
        for t in range(_data_.cnt.T):
            if p in _data_.inf.PT[t]: d += 1

    return d
#########################

cst_list = []

def createCST():
    cst_list.append(CST(alpha_1, m_1, d_1, indexQBitW))
    cst_list.append(CST(alpha_2, m_2, d_2, indexQBitT))
    cst_list.append(CST(alpha_3, m_3, d_3, indexQBitT))
    cst_list.append(CST(alpha_4, m_4, d_4, indexQBitT))
    cst_list.append(CST(alpha_5, m_5, d_5, indexQBitT))
    cst_list.append(CST(alpha_6, m_6, d_6, indexQBitT))
    cst_list.append(CST(alpha_7, m_7, d_7, indexQBitT))