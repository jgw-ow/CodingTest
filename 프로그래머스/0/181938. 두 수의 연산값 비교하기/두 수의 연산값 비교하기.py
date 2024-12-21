def solution(a, b):
    add = int(str(a) + str(b))
    multy = 2*a*b
    return add if add > multy else multy if add < multy else add