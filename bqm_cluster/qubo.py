import math

ancillaryIndexOffset = 0
lagrangeFactor = 1

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

def EquQUBO(bqm, cst):
    indexQBit_f = cst.i_f

    alpha = cst.alpha_f()
    m_f = cst.m_f

    l_f = getLagrangeFactor()

    for i in alpha: #q
        m_i = m_f(i)
        if m_i != 0:
            fi = m_i**2
            bqm.add_linear(indexQBit_f(i), l_f*fi)

    for index, i in enumerate(alpha): #qq
        m_i = m_f(i)
        if m_i != 0:
            for j in alpha[index+1:]:
                m_j = m_f(j)
                if m_j != 0:
                    fij = 2*m_i*m_j
                    bqm.add_quadratic(indexQBit_f(i), indexQBit_f(j), l_f*fij)

def IneQUBO(bqm, cst):

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
            bqm.add_linear(indexQBit_f(i), l_f*fi)

    for index, i in enumerate(alpha): #qq
        m_i = m_f(i)
        if m_i != 0:
            for j in alpha[index+1:]:
                m_j = m_f(j)
                if m_j != 0:
                    fij = 2*m_i*m_j
                    bqm.add_quadratic(indexQBit_f(i), indexQBit_f(j), l_f*fij)

    for i in alpha: #qa
        m_i = m_f(i)
        if m_i != 0:
            for k in range(nb_l, nb_m):
                fi = m_i*(2**(k+1))
                bqm.add_quadratic(indexQBit_f(i), offset+(k-nb_l), l_f*fi)


    for k in range(nb_l, nb_m): #a
        fi = (2**(2*k))-d*(2**(k+1))
        bqm.add_linear(offset+(k-nb_l), l_f*fi)

    for k in range(nb_l, nb_m): #aa
        for t in range(k+1, nb_m):
            fi = 2**(k+t+1)
            bqm.add_quadratic(offset+(k-nb_l), offset+(t-nb_l), l_f*fi)

    setAncillaryIndexOffset(offset+(nb_m-nb_l))

def qubo(bqm, cst):
    d = cst.d_f()

    if d == 0:
        EquQUBO(bqm, cst)
    else:
        IneQUBO(bqm, cst)
