def solution(n, m):
    measure = []
    for i in range(1, max([n, m])+1):
        if n%i==0 and m%i==0:
            measure.append(i)
    return [max(measure), n*m//max(measure)]