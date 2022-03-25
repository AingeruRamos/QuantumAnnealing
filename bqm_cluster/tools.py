import openpyxl
from pathlib import Path
import struct
import enum
import psutil

class SIZE_UNIT(enum.Enum):
   BYTES = 1
   KB = 2
   MB = 3
   GB = 4

def chargeXLSXFile(file_path):
    xlsx_file = Path('', file_path)
    wb = openpyxl.load_workbook(xlsx_file)
    return wb.active
    
def getWeek(date):
    return date.strftime("%W")

def writeDoubleInBinaryFile(fd, n):
    fd.write(struct.pack('d', n))

def readDoubleInBinaryFile(fd):
    aux = struct.unpack('d', fd.read(8))
    return aux[0]

def convert_unit(size_in_bytes, unit):
   if unit == SIZE_UNIT.MB:
       return size_in_bytes/(1024*1024)
   elif unit == SIZE_UNIT.GB:
       return size_in_bytes/(1024*1024*1024)
   else:
       return size_in_bytes

def printRAMUsage():
    m = psutil.virtual_memory().used
    m = format(convert_unit(m, SIZE_UNIT.GB), '.2f')
    print(f"{m} GB")
