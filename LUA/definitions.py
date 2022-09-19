import sys
import math
import random


class Sym:

    def __init__(self, *args):
        self.n = 0
        self.at = 0
        self.name = ''
        if len(args) > 0:
            self.at = args[0]
            self.name = args[1]
        self._has = {}

    def add(self, v):
        v = str(v)
        if v != '?':
            self.n += 1
            if v in self._has.keys():
                self._has[v] += 1
            else:
                self._has[v] = 1

    def mid(self):
        max = -1
        mode = -1
        for sym, count in self._has.items():
            if count > max:
                max = count
                mode = sym
        return mode

    def div(self):
        e = 0
        for sym, count in self._has.items():
            if count > 0:
                p = count / self.n
                e = e - p * math.log2(p)
        return e


t = [1, 2, 2, 31, 1, 1, 6, 5]


class Num:

    def __init__(self, *args):
        self.n = 0
        self.at = 0
        self.name = ''
        if len(args) > 0:
            self.at = args[0]
            self.name = args[1]
        self._has = {}
        self.lo = -sys.maxsize - 1
        self.high = sys.maxsize
        self.isSorted = True
        # self.w = (args[1] or '').find('-$') == -1 and -1 or 1

    def nums(self):
        if not self.isSorted:
            print(self._has)
            self._has = dict(sorted(list(self._has.items())))
            print(self._has)
            self.isSorted = True
        return self._has

    # per
    def per(self, t, *args):
        p = math.floor(((len(args) > 0 and args[0] or 0.5) * len(t)) + 0.5)
        return t[max(1, min(len(t), p))]

    # Num Add
    def add(self, v, the):
        if type(v) == int:
            self.n += 1
            self.lo = min(v, self.lo)
            self.high = max(v, self.high)
            pos = None
            if len(self._has) < the['nums']:
                pos = 1 + len(self._has)
            elif random.random() < the['nums'] / self.n:
                pos = random.randint(0, len(self._has))

            if pos:
                self.isSorted = False
                self._has[pos] = int(v)
        else:
            print("Symbol encountered!!")

    # Num Div
    def div(self):
        a = self.nums()
        return (self.per(a, 0.9) - self.per(a, 0.1)) / 2.58

    # Num Mid
    def mid(self):
        return self.per(self.nums(), 0.5)

    @property
    def has(self):
        return self._has
