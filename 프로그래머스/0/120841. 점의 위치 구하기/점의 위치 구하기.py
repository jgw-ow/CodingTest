def solution(dot):
    x = dot[0]
    y = dot[1]
    result = 0
    if x > 0 and y > 0:
        result += 1
    elif x < 0 and y < 0:
        result += 3
    elif x < 0 and y > 0:
        result += 2
    else:
        result += 4
    return result