def solution(n, k):
    for i in range(1, n+1):
        if i%10==0:
            k -= 1
    return n*12000 + k*2000
