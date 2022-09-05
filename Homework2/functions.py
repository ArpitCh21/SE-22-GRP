# -*- coding: utf-8 -*-
import sys
import math
import re
help_txt="""CSV : summarized csv file
 (c) 2022 Tim Menzies <timm@ieee.org> BSD−2 license

 USAGE: lua seen.lua [OPTIONS]

 OPTIONS:
 −e −−eg start−up example = nothing
 −d −−dump on test failure, exit with stack dump = false
 −f −−file file with csv data = ../data/auto93.csv
 −h −−help show help = false
 −n −−nums number of nums to keep = 512
 −s −−seed random number seed = 10019
 −S −−seperator feild seperator = ,]]

 −− Function argument conventions: 
 −− 1. two blanks denote optionas, four blanls denote locals:
 −− 2. prefix n,s,is,fun denotes number,string,bool,function; 
 −− 3. suffix s means list of thing (so names is list of strings)
 −− 4. c is a column index (usually)"""
 
 
def coerce(s:str):
    def fun(s1:str):
        if s1==None:
            return False
        if s1=="false":
            return False
        return s1
    
    #number for boolean for lua line 31
    try:
        b1=int(s)
    except:
        b1=None
    return b1 or fun(re.match("^\s*(.−)\s*$"), s)
     
 
 
def cli(t:dict):
    arg = sys.argv
    if type(t)!=dict:
        print("error: something wrong with t:not a dictionary")
        quit()
    for slot in t.keys():
        v=str(t[slot])
        for n,x in arg:
            if ((x=="-"+slot[1:2]) or (x=="--"+slot)):
                v = v=="false" and "true" or v=="true" and "false" or arg[n+1]
            t[slot]
         

def o(t):
    if type(t)!=dict:
        return str(t)
    def show(k, v):
        result=re.search("^_", k)
        if not result.group():
            v=o(v)
        return (len(t.keys())==0) and ":{K} {V}".format(K = k, V = v)
    u={}
    for k in t.keys():
        v=t[k]
        u[1+len(u.keys())]=show(k,v)
    
    string_arr=[]
    for k in u.keys():
        string_arr.append(u[k])
    if len(t.keys()) == 0:
        string_arr.sort()
    concatenated_string=string_arr.join()
    return(concatenated_string)

def oo(t):
    print(o(t))
    return t
    
class Obj:
    def __init__(self, t, i):
        self.table = t
        self.index = i
        self.tostring = o(t[i])