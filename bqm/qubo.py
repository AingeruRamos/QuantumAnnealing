import math

ancillaryIndexOffset = 0
lagrangeFactor = 0

def getFixCommaLessBitIndex(frac_value):
    nl = 0
    for i in range(4):
        frac_value *= 2
        if frac_value >= 1:
            frac_value -= 1
        elif frac_value == 0:
            break
        nl += 1
    return -1*nl

def setAncillaryIndexOffset(offset):
    global ancillaryIndexOffset
    ancillaryIndexOffset = offset

def getAncillaryIndexOffset():
    return ancillaryIndexOffset

def setLagrangeFactor(l_f):
    global lagrangeFactor
    lagrangeFactor = l_f

def getLagrangeFactor():
    return lagrangeFactor

def addToQ(Q, key, value):
    dir_id = key[0]
    if not dir_id in Q:
        Q[dir_id] = {}
        
    if not key[1] in Q[dir_id]:
        Q[dir_id][key[1]] = value
    else:
        Q[dir_id][key[1]] += value 

def EquQUBO(Q, cst):
    indexQBit_f = cst.i_f

    alpha = cst.alpha_f()
    m_f = cst.m_f

    l_f = getLagrangeFactor()

    for i in alpha: #q
        m_i = m_f(i)
        if m_i != 0:
            fi = m_i**2
            addToQ(Q, (indexQBit_f(i), indexQBit_f(i)), l_f*fi)

    for index, i in enumerate(alpha): #qq
        m_i = m_f(i)
        if m_i != 0:
            for j in alpha[index+1:]:
                m_j = m_f(j)
                if m_j != 0:
                    fij = 2*m_i*m_j
                    addToQ(Q, (indexQBit_f(i), indexQBit_f(j)), l_f*fij) 

def IneQUBO(Q, cst):

    indexQBit_f = cst.i_f

    alpha = cst.alpha_f()

    m_f = cst.m_f
    d = cst.d_f()

    nb_m = math.ceil(math.log2(d)) + 1
    frac_value = d - math.floor(d)
    nb_l = getFixCommaLessBitIndex(frac_value)

    offset = getAncillaryIndexOffset()
    l_f = getLagrangeFactor()

    for i in alpha: #q
        m_i = m_f(i)
        if m_i != 0:
            fi = (m_i**2)-2*d*m_i
            addToQ(Q, (indexQBit_f(i), indexQBit_f(i)), l_f*fi)

    for index, i in enumerate(alpha): #qq
        m_i = m_f(i)
        if m_i != 0:
            for j in alpha[index+1:]:
                m_j = m_f(j)
                if m_j != 0:
                    fij = 2*m_i*m_j
                    addToQ(Q, (indexQBit_f(i), indexQBit_f(j)), l_f*fij)

    for i in alpha: #qa
        m_i = m_f(i)
        if m_i != 0:
            for k in range(nb_l, nb_m):
                fi = m_i*(2**(k+1))
                addToQ(Q, (indexQBit_f(i), offset+(k-nb_l)), l_f*fi)

    for k in range(nb_l, nb_m): #a
        fi = (2**(2*k))-d*(2**(k+1))
        addToQ(Q, (offset+(k-nb_l), offset+(k-nb_l)), l_f*fi)

    for k in range(nb_l, nb_m): #aa
        for t in range(k+1, nb_m):
            fi = 2**(k+t+1)
            addToQ(Q, (offset+(k-nb_l), offset+(t-nb_l)), l_f*fi)

    #Algo con el d^2

    setAncillaryIndexOffset(offset+(nb_m-nb_l))

def qubo(Q, cst):
    d = cst.d_f()

    if d == 0:
        EquQUBO(Q, cst)
    else:
        IneQUBO(Q, cst)