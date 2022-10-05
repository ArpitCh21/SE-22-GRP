import sys
sys.path.append("./code")
from functions import copy


class Rows:

    def __init__(self, t:dict):
        self.cells = t
        self.cooked = copy(t)
        self.isEvaled = False

