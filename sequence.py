'''
sequence modules
'''
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
