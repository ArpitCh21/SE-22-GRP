# -*- coding: utf-8 -*-
import sys
import math
import re as reg

the={'eg':'','dump':False,'file':'./data/auto93.csv','help':False,'nums':512,'seed':10019,'seperator':','}

help = """usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-b     : issue warnings about str(bytes_instance), str(bytearray_instance)
         and comparing bytes/bytearray with str. (-bb: issue errors)
-B     : don't write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x
-c cmd : program passed in as string (terminates option list)
-d     : turn on parser debugging output (for experts only, only works on
         debug builds); also PYTHONDEBUG=x
-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
-h     : print this help message and exit (also -? or --help)
-i     : inspect interactively after running script; forces a prompt even
         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
-I     : isolate Python from the user's environment (implies -E and -s)
-m mod : run library module as a script (terminates option list)
-O     : remove assert and __debug__-dependent statements; add .opt-1 before
         .pyc extension; also PYTHONOPTIMIZE=x
-OO    : do -O changes and also discard docstrings; add .opt-2 before
         .pyc extension
-q     : don't print version and copyright messages on interactive startup
-s     : don't add user site directory to sys.path; also PYTHONNOUSERSITE
-S     : don't imply 'import site' on initialization
-u     : force the stdout and stderr streams to be unbuffered;
         this option has no effect on stdin; also PYTHONUNBUFFERED=x
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
         when given twice, print more information about the build
-W arg : warning control; arg is action:message:category:module:lineno
         also PYTHONWARNINGS=arg
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
-X opt : set implementation-specific option. The following options are available:
         -X faulthandler: enable faulthandler
         -X showrefcount: output the total reference count and number of used
             memory blocks when the program finishes or after each statement in the
             interactive interpreter. This only works on debug builds
         -X tracemalloc: start tracing Python memory allocations using the
             tracemalloc module. By default, only the most recent frame is stored in a
             traceback of a trace. Use -X tracemalloc=NFRAME to start tracing with a
             traceback limit of NFRAME frames
         -X importtime: show how long each import takes. It shows module name,
             cumulative time (including nested imports) and self time (excluding
             nested imports). Note that its output may be broken in multi-threaded
             application. Typical usage is python3 -X importtime -c 'import asyncio'
         -X dev: enable CPython's "development mode", introducing additional runtime
             checks which are too expensive to be enabled by default. Effect of the
             developer mode:
                * Add default warning filter, as -W default
                * Install debug hooks on memory allocators: see the PyMem_SetupDebugHooks()
                  C function
                * Enable the faulthandler module to dump the Python traceback on a crash
                * Enable asyncio debug mode
                * Set the dev_mode attribute of sys.flags to True
                * io.IOBase destructor logs close() exceptions
         -X utf8: enable UTF-8 mode for operating system interfaces, overriding the default
             locale-aware mode. -X utf8=0 explicitly disables UTF-8 mode (even when it would
             otherwise activate automatically)
         -X pycache_prefix=PATH: enable writing .pyc files to a parallel tree rooted at the
             given directory instead of to the code tree
         -X warn_default_encoding: enable opt-in EncodingWarning for 'encoding=None'
--check-hash-based-pycs always|default|never:
    control how Python invalidates hash-based .pyc files
file   : program read from script file
-      : program read from stdin (default; interactive mode if a tty)
arg ...: arguments passed to program in sys.argv[1:]"""


def coerce(s: str):

    if(reg.search(r'\d',s)):
        return float(s)
    return s



def cli(t: dict) -> dict:
    arg = sys.argv
    if type(t) != dict:
        print("error: something wrong with t:not a dictionary")
        quit()
    for slot in t.keys():
        v = str(t[slot])
        for n, x in arg:
            if ((x == "-" + slot[1:2]) or (x == "--" + slot)):
                v = v == "false" and "true" or v == "true" and "false" or arg[n + 1]
            t[slot] = coerce(v)
    if (x == "-h" or x == "--help"):
        print("\n")
        print(help)
        print("\n")

    return t


def copy(t:dict):
    if type(t)!=dict:
        return t
    u = {}
    for k in t.keys():
        u[k] = copy(t[k])
    return u


def per(t,p):
    p=math.floor(((0.5 if p is None else p)*len(t))+0.5)
    return t[max(1,min(len(t),p))]

def push(t,x):
    t[1+len(t.keys())]=x
    return x


def csv(fileName):
    if(fileName==None or len(fileName.strip())==0):
        raise Exception("FILE NOT FOUNDED")
    rows=[]
    with open(fileName,'r',encoding='utf-8') as file:
        row_eles=file.readlines()
        for row_ele in row_eles:
            k=list(map(coerce,row_ele.split(',')))
            rows.append(k)
    return rows


def o(t: dict) -> str:
    print(t)
    if type(t) != dict:
        return str(t)

    def show(k, v):
        if reg.search("^_", str(k)) is not None:
            if not reg.search("^_", str(k)).group():
                v = o(v)
        return (len(t.keys()) != 0) and ":{K} {V}".format(K=k, V=v)

    u = {}
    if len(t.keys())==0:
        return("nothing to print")

    for k in t.keys():
        v = t[k]
        u[1 + len(u.keys())] = show(k, v)

    string_arr = []
    # print(u)
    for k in u.keys():
        string_arr.append(u[k])
    if len(t.keys()) == 0:
        string_arr.sort()
    # print(string_arr)
    concatenated_string = ''.join(string_arr)
    return (concatenated_string)


def oo(t: dict) -> dict:
    print(o(t))
    return t


def rnd(x, places):
    mult = 10 ** (places or 2)
    return (math.floor(x * mult + 0.5) / mult)


class Obj:
    def __init__(self, t, i):
        self.table = t
        self.index = i
        self.tostring = o(t[i])
