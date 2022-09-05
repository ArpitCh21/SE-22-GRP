import sys


def sym_new(c:int, s:str):
    return {'n': 0, 'at': c or 0, 'name': s or '', '_has': {}}


def num_new(c:int, s:str):
    return {'n': 0, 'at': c or 0, 'name': s or '', '_has': {}, 'lo': -sys.maxsize - 1, 'high': sys.maxsize,
            'isSorted': True, 'w': (s or '').find('-$') == -1 and -1 or 1}
