import csv
import math
import io
class CsvFile:

    def __init__(self, the, t):
        self.t = the


    def csv(self, fname, fun, sep, src, s, t):
        sep = "([^" ..the.separator.. "]+)"
        src = input(fname)
        while True:
            s = io.read()
            if not s:
                return io.close(src)
            else:
                t = {}
                for s1 in s.gmatch(sep):
                    t[1+t] = coerce(s1)
        fun(t)
