from dataContainer import _data_
from qubo import getLagrangeFactor, getAncillaryIndexOffset

res_counter = 0
max_res_counter = 0
res_id = 0

def setAuxInfo(max_res, id=-1):
    global res_counter
    global max_res_counter
    global res_id

    res_counter = 1
    max_res_counter = max_res
    res_id = id

def printAuxInfo(msg=None):
    global res_counter

    if msg == None:
        print(f"\rRestricción {res_id} > {max_res_counter}/{res_counter}", end='')
    else:
        print(f"\r{msg} > {max_res_counter}/{res_counter}", end='')
        
    res_counter += 1

    if res_counter > max_res_counter: print()

def printCNT():
    print("W: {}, T: {}, D: {}, S: {}\nlagrangeFactor: {}, ancillaryOffset: {}"
                                                    .format(_data_.cnt.W, _data_.cnt.T, 
                                                            _data_.cnt.D, _data_.cnt.S,
                                                            getLagrangeFactor(), 
                                                            getAncillaryIndexOffset()))