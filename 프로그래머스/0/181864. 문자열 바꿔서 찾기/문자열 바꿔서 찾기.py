def solution(myString, pat):
    rev_str = ''
    for i in range(0, len(myString)):
        if myString[i] == 'A':
            rev_str += 'B'
        else:
            rev_str += 'A'
    if pat in rev_str:
        return 1
    else:
        return 0