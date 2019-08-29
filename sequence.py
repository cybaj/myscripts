'''
sequence modules
'''
import math

def get_zero_matrix(i, j):
    '''
    returns zeros 2d matrix.
    '''
    matrix = []
    for _i in range(i):
        matrix.append([])
        for _j in range(j):
            matrix[_i].append(0)
    return matrix


def evens(seq):
    '''
    returns sequence of even members.
    '''
    for i in range((len(seq) - 1) // 2 + 1):
        seq.pop(i)
    return seq


def odds(seq):
    '''
    returns sequence of odd members.
    '''
    for i in range(1, ((len(seq) - 1) // 2)):
        seq.pop(i)
    return seq

def triples(seq):
    '''
    returns sequence of triple members.
    '''
    lmt = math.ceil((len(seq) - len(seq) // 3) / 2)
    rmd = (len(seq) % 3)
    for i in range(0, lmt):
        seq.pop(i)
        if lmt - 1 == i and not rmd == 0:
            for _ in range(1, rmd):
                seq.pop(i)
        else:
            seq.pop(i)
    return seq

def n_steps(n_s, seq):
    '''
    returns sequence of n-step members.
    '''
    lmt = math.ceil((len(seq) - len(seq) // n_s) / (n_s - 1))
    rmd = (len(seq) % n_s)
    print(lmt)
    print(rmd)
    for i in range(0, lmt):
        seq.pop(i)
        if lmt - 1 == i and not rmd == 0:
            for _ in range(1, rmd):
                seq.pop(i)
        else:
            for _ in range(n_s - 2):
                seq.pop(i)
    return seq
