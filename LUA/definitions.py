import sys
import math
import random
from functions import *


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


class Cols:

    def init(self,names):
        self.names=names
        self.all=[]
        self.klass=None
        self.x=[]
        self.y=[]

        for column_name in self.names:
            if column_name[0].isupper():
                column=Num(names.index(column_name),column_name)
            else:
                column=Sym(names.index(column_name),column_name)

            if column_name[-1]!=':':
                if('!' in column_name or '+' in column_name or '-' in column_name):
                    self.y.append(column)
                else:
                    self.x.append(column)

            if column_name[-1]=='!':
                self.klass=column
            self.all.append(column)

    def str(self):
        return f"names is {self.names}, all is {self.all}, klass is {self.klass}, x is {self.x}, y is {self.y}"


class Rows:

    def __init__(self, t:dict):
        self.cells = t
        self.cooked = copy(t)
        self.isEvaled = False


class Data: 

    def init(self,src):
        self.cols=None
        self.rows=[]
        self.src=src
        if type(self.src) == str:
            self.src=csv(src)
            for row in self.src:
                self.add(row)
        else:
            for row in self.src:
                self.add(row)

    def add(self,xs):

        if not self.cols:
            self.cols=Cols(xs)
        else:
            if type(xs)!= Rows:
                row=Rows(xs)
            else:
                row=xs
            self.rows.append(row)
            for i in [self.cols.x,self.cols.y]:
                for j in i:
                    j.add(row.cells[j.at])


    def stats(self,column,fun='mid'):
        if(column=='x'):
            showCols=self.cols.x
        if(column=='y'):
            showCols=self.cols.y
        t={}
        for i in showCols:
            if(type(i)==Num):
                if(fun=='mid'):
                    v=i.mid()
                elif(fun=='div'):
                    v=i.div()
            t[i.name]=v
        return t


    @property
    def has(self):
        return self._has
