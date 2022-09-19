import random
import math


# Num nums
class Num:
    n = 0

    def __init__(self, the, _has):
        self.t = the
        self._has = _has
        self.lo = -math.inf
        self.hi = math.inf
        self.isSorted = True

    def nums(self):
        if not self.isSorted:
            self.t.sort(self._has)
            self.isSorted = True

        return self._has

    # per
    def per(self, t, p):
        p = math.floor(((p or 0.5) * self.t) + 0.5)
        return t[max(1, min(self.t, p))]

    # Num Add
    def add(self, v, pos):
        if type(v) == int or type(v) == float:
            self.n += 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)

            if self._has < self.t.nums:
                pos = 1 + self._has
            elif random.random() < self.t.nums / self.n:
                pos = self._has - 1

            if pos:
                self.isSorted = False
                self._has[pos] = int(v)
        else:
            print("Symbol encountered!!")

    # Num Div
    def div(self, a):
        a = self.nums()
        return (self.per(a, 0.9) - self.per(a, 0.1)) / 2.58

    # Num Mid
    def mid(self):
        return self.per(self.nums(), 0.5)





