import sys
import math
import random
from functions import *


class Sym:
    def __init__(self,c=0,s='') -> None:
        self.n = 0
        self.name=s
        self.at=c
        self._has = dict()

    
    def add(self, v):
        if v != '?':
            self.n = self.n + 1
            self._has[v] = 1 + self._has.get(v, 0)


    def mid(self):
        return max(self._has, key=self._has.get)
    

    def div(self):
        fun = lambda p : p*math.log(p,2)
        e = 0  
        for key in self._has.keys():
            if self._has[key] > 0 :
                e = e - fun(self._has[key]/self.n)
        
        return e


class Num:
    
    #'Num' summarizes the stream of numbers
    def __init__(self,c=0,s=str()):
        self.n=0
        self.at=c
        self.name=s
        self._has=dict()
        self.low=math.inf
        self.high=-math.inf
        self.isSorted=True
        if(len(s)>0 and s[-1]=='-'):
            self.w=-1
        else:
            self.w=1
    
    def __str__(self):
        return "{"+ f" n:{self.n}, at:{self.at+1}, name:{self.name}, low:{self.low}, high:{self.high}, isSorted:{self.isSorted}, w:{self.w}"+"}"

    #Return kept numbers, sorted.
    def nums(self):
        if (not self.isSorted):
            list(sorted(self._has))
        return self._has
            
        

    #Reservoir sampler. Keep atmost 'the[nums]' numbers 
    # (if we run out of space delete something old at random and add new)
    def add(self,ele,pos=None):
        if ele!='?':
            self.n=self.n+1
            self.low=min(self.low,int(ele))
            self.high=max(self.high,int(ele))
            if ( (len(self._has))<(the['nums']) ):
                pos=1+len(self._has)
            elif ( random.randint(0,len(self._has)) < (the['nums'])/self.n ):
                pos=random.randint(1,len(self._has))
            if pos!=None:
                self.isSorted=False
                self._has[pos]=int(ele)


    #Diversity (standard deviation from Nums, entropy for Syms)
    def div(self):
        a=self.nums()
        return (per(a,0.9)-per(a,0.1))/2.58 
    
    #Central tendency (median for Nums, mode for Syms)
    def mid(self):
        return per(self.nums(),0.5) 

class Data: 
    
    def __init__(self,src):
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
        s = Sym()
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


class Cols:

    def __init__(self,names):
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
    
    def __str__(self):
        return f"names is {self.names}, all is {self.all}, klass is {self.klass}, x is {self.x}, y is {self.y}"


class Rows:

    def __init__(self, t:dict):
        self.cells = t
        self.cooked = copy(t)
        self.isEvaled = False

