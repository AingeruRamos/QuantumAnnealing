import openpyxl
from pathlib import Path
import struct

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