import sys


class Sym():
    def _init_(self, c: int, s: str):
        self.n = 0
        self.at = c or 0
        self.name = s or ''
        self._has = {}


class Num():
    def _init_(self, c: int, s: str):
        self.n = 0
        self.at = c or 0
        self.name = s or ''
        self._has = {}
        self.lo = -sys.maxsize - 1
        self.high = sys.maxsize
        self.isSorted = True
        self.w = (s or '').find('-$') == -1 and -1 or 1

        
class Rows():
    def __init__(self, t:dict):
        self.cells = t
        self.cooked = copy(t)
        self.isEvaled = False
