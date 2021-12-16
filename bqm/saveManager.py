import os
import ast
from qubo.qubo import getAncillaryIndexOffset
import debug as dbug
from tools import readDoubleInBinaryFile, writeDoubleInBinaryFile

def createEnviroment(dir_path):
    os.mkdir(dir_path)
    open(f"{dir_path}/keys", 'w').close()
    open(f"{dir_path}/values", 'wb').close()

def saveQ(Q):
    last_debug_len = 0
    debug_str = ""

    max_dir_id = getAncillaryIndexOffset()
    for dir_name in range(max_dir_id):
        
        if not dir_name in Q: continue

        dir_path = "Q/{}".format(str(dir_name))
        if not os.path.isdir(dir_path):
            createEnviroment(dir_path)

        with open(f"{dir_path}/keys", 'r+') as fd_key, open(f"{dir_path}/values", 'r+b') as fd_val:
            
            key_list = ast.literal_eval('{' + fd_key.read() + '}')
            n_keys = len(key_list)

            for key, value in Q[dir_name].items():
                
                value_index = 0

                if not key in key_list:
                    value_index = n_keys
                    fd_key.write(f"{key}:{value_index},")
                    n_keys += 1
                else:
                    value_index = key_list[key]
                    fd_val.seek(8*value_index)
                    value += readDoubleInBinaryFile(fd_val)

                fd_val.seek(8*value_index)
                writeDoubleInBinaryFile(fd_val, value)

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
            key_list = ast.literal_eval('{' + fd_key.read() + '}')

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