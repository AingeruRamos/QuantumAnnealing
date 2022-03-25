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
    return range(_data_.cnt.W)

def m_1(w):
    return _data_.inf.HT[_data_.aux.selectedT]

def d_1():
    return _data_.inf.HT[_data_.aux.selectedT]
#########################
def alpha_2():
    t_interval_start, t_interval_end = _data_.inf.D[_data_.aux.selectedD]
    return range(t_interval_start, t_interval_end+1)

def m_2(t):
    return _data_.inf.HT[t]

def d_2():
    t_interval_start, t_interval_end = _data_.inf.D[_data_.aux.selectedD]
    
    max_ht = -1
    for t in range(t_interval_start, t_interval_end+1):
        if _data_.inf.HT[t] > max_ht:
            max_ht = _data_.inf.HT[t]

    return max_ht
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
    return _data_.inf.JP[t]*_data_.inf.HT[t]

def d_6():
    t_interval_start, t_interval_end = _data_.inf.S[_data_.aux.selectedS]
    
    max_ht = -1
    for t in range(t_interval_start, t_interval_end+1):
        if _data_.inf.HT[t] > max_ht:
            max_ht = _data_.inf.JP[t]*_data_.inf.HT[t]
    
    return max_ht
#########################
def alpha_7():
    return _data_.inf.PWT[_data_.aux.selectedW]

def m_7(t):
    return 1

def d_7():
    return 0
#########################

cst_list = [CST(alpha_1, m_1, d_1, indexQBitW), 
            CST(alpha_2, m_2, d_2, indexQBitT), 
            CST(alpha_3, m_3, d_3, indexQBitT), 
            CST(alpha_4, m_4, d_4, indexQBitT), 
            CST(alpha_5, m_5, d_5, indexQBitT),
            CST(alpha_6, m_6, d_6, indexQBitT),
            CST(alpha_7, m_7, d_7, indexQBitT)]
