from dataContainer import _data_
import tools as tls
from datetime import timedelta
import re

def chargeHTInf(t_sheet):
    for row in t_sheet.iter_rows(min_row=2, min_col=5, max_col=5):
        _data_.inf.HT.append(row[0].value)

def chargeDInf(t_sheet):
    day_value = ''
    t_counter_init = 0
    t_counter_last = -1
    for row in t_sheet.iter_rows(min_row=2, min_col=4, max_col=4):
        if row[0].value != day_value:
            if day_value != '':
                _data_.inf.D.append([t_counter_init, t_counter_last])
                t_counter_init = t_counter_last+1
            day_value = row[0].value
        t_counter_last += 1

    _data_.inf.D.append([t_counter_init, t_counter_last])

def chargeSInf(t_sheet):
    actual_week = -1
    t_counter_init = 0
    t_counter_last = -1
    for row in t_sheet.iter_rows(min_row=2, min_col=4, max_col=4):
        aux = tls.getWeek(row[0].value)
        if aux != actual_week:
            if actual_week != -1:
                _data_.inf.S.append([t_counter_init, t_counter_last])
                t_counter_init = t_counter_last+1
            actual_week = aux
        t_counter_last += 1

    _data_.inf.S.append([t_counter_init, t_counter_last])

def chargeJPInf(t_sheet):
    t = 0
    for row in t_sheet.iter_rows(min_row=2, min_col=7, max_col=8):
        work_start = row[0].value
        work_end = row[1].value

        total_work = work_end - work_start

        ht = timedelta(hours=_data_.inf.HT[t])

        if total_work > ht:
            _data_.inf.JP.append(1)
        else:
            _data_.inf.JP.append(0)

        t += 1

def chargeHAInf(w_sheet):
    for row in w_sheet.iter_rows(min_row=2, min_col=16, max_col=16):
        _data_.inf.HA.append(row[0].value)

def chargeHSInf(w_sheet):
    for days in _data_.inf.SW:
        _data_.inf.HS.append(8*days)

def chargeSWInf(w_sheet):
    for row in w_sheet.iter_rows(min_row=2, min_col=7, max_col=7):
        _data_.inf.SW.append(7-row[0].value)

def chargePTW(t_sheet, w_sheet):
    PT = []
    for row in t_sheet.iter_rows(min_row=2, min_col=6, max_col=6):
        str = re.sub(r'[\[\]]', '', row[0].value)
        str = re.sub(r' ', '', str)
        p_values = str.split(',')
        PT.append(p_values)

    PW = []
    for row in w_sheet.iter_rows(min_row=2, min_col=15, max_col=15):
        str = re.sub(r'[\[\]\(\)]', '', row[0].value)
        str = re.sub(r' ', '', str)
        p_values = str.split(',')
        PW.append(p_values)

    for pw in PW:
        t_indexes = []
        for index, pt in enumerate(PT):
            pw_set = set(pw)
            pt_set = set(pt)
            pwt_set = pw_set.intersection(pt_set)
            if len(pwt_set) == 0:
                t_indexes.append(index)
        _data_.inf.PWT.append(t_indexes)

def initCNTValues(t_sheet, w_sheet):

    _data_.cnt.W = w_sheet.max_row-1
    _data_.cnt.T = t_sheet.max_row-1
    _data_.cnt.D = len(_data_.inf.D)
    _data_.cnt.S = len(_data_.inf.S)

def restartAux():
    _data_.aux.selectedW = -1
    _data_.aux.selectedT = -1
    _data_.aux.selectedS = -1
    _data_.aux.selectedD = -1

def chargeData():

    t_sheet = tls.chargeXLSXFile('../data/jornadas_11.xlsx')
    w_sheet = tls.chargeXLSXFile('../data/trabajadores_11.xlsx')
    
    chargeHTInf(t_sheet)
    chargeDInf(t_sheet)
    chargeSInf(t_sheet)
    chargeJPInf(t_sheet)

    chargeHAInf(w_sheet)

    chargeSWInf(w_sheet)
    chargeHSInf(w_sheet)

    chargePTW(t_sheet, w_sheet)

    initCNTValues(t_sheet, w_sheet)

    restartAux()