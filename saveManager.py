import os
import ast
from qubo import getAncillaryIndexOffset
import debug as dbug
from tools import readDoubleInBinaryFile, writeDoubleInBinaryFile

def saveQ(Q):
    last_debug_len = 0
    debug_str = ""

    max_dir_id = getAncillaryIndexOffset()
    for dir_name in range(max_dir_id):
        
        if not dir_name in Q: continue

        dir_path = "Q/{}".format(str(dir_name))
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
            with open(f"{dir_path}/keys", 'w') as fd_key, open(f"{dir_path}/values", 'wb'):
                fd_key.write('{ }')

        fd_key = open(f"{dir_path}/keys", 'r+')
        fd_val = open(f"{dir_path}/values", 'r+b')

        key_list = ast.literal_eval(fd_key.read())

        for key, value in Q[dir_name].items():
            
            value_index = 0
            next_value = value

            if not key in key_list:
                key_list[key] = len(key_list)
                value_index = key_list[key]
            else:
                value_index = key_list[key]
                fd_val.seek(8*value_index)
                next_value += readDoubleInBinaryFile(fd_val)

            fd_val.seek(8*value_index)
            writeDoubleInBinaryFile(fd_val, next_value)

        fd_val.close()

        fd_key.seek(0)
        fd_key.write('{')
        for key, value in key_list.items():
            fd_key.write(f"{key}:{value},")
        fd_key.seek(fd_key.tell()-1, os.SEEK_SET)
        fd_key.write('}')
        fd_key.truncate()
        fd_key.close()

        debug_str = f"\rSaving Q: {dir_name}"

        if len(debug_str) < last_debug_len:
            print("\r", end='', flush=True)
            [print(' ', end='', flush=True) for _ in range(last_debug_len)]

        print(debug_str, end='')
        last_debug_len = len(debug_str)

    print()

def makeUnion():

    dirs = os.listdir('./Q')

    dbug.setAuxInfo(len(dirs))

    fd_Q = open('./Q/Q_final', 'w')
    fd_Q.write('{')

    for dir_name in dirs:

        dir_path = f"./Q/{dir_name}"

        dbug.printAuxInfo("Binding Files")
        
        key_list = {}
        with open(f"{dir_path}/keys") as fd_key:
            key_list = ast.literal_eval(fd_key.read())

        with open(f"{dir_path}/values", 'rb') as fd_val:
            for key, value_index in key_list.items():
                fd_val.seek(8*value_index)
                value = readDoubleInBinaryFile(fd_val)
                fd_Q.write(f"({dir_name},{key}):{value},")

        os.remove(f"{dir_path}/keys") 
        os.remove(f"{dir_path}/values") 
        os.rmdir(dir_path)

    fd_Q.seek(fd_Q.tell()-1, os.SEEK_SET)
    fd_Q.write('}')
    fd_Q.close()