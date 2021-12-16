class Constants:
    def __init__(self):
        self.T = 0
        self.W = 0
        self.D = 0
        self.S = 0

class Auxiliary:
    def __init__(self):
        self.selectedT = 0
        self.selectedW = 0
        self.selectedD = 0
        self.selectedS = 0

class Info:
    def __init__(self):
        self.D = []
        self.S = []
        self.HT = []
        self.HA = []
        self.HS = []
        self.SW = []
        self.JP = []
        self.PWT= []

class Data:
    def __init__(self):
        self.cnt = Constants()
        self.aux = Auxiliary()
        self.inf = Info()

_data_ = Data()