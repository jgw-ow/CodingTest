def solution(s):
    low = []
    up = []
    for i in s:
        if i == i.lower():
            low += i
        else:
            up += i
    return ''.join(sorted(low, reverse = True)) + ''.join(sorted(up, reverse = True))