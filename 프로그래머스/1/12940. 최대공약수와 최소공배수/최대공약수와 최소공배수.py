# def solution(n, m):
#     measure = []
#     for i in range(1, max([n, m])+1):
#         if n%i==0 and m%i==0:
#             measure.append(i)
#     return [max(measure), n*m//max(measure)]
def solution(n, m):
    gcd = lambda a,b: b if a % b == 0 else gcd(b, a%b)
    lcm = lambda a,b: n*m//gcd(a, b)
    return [gcd(n,m), lcm(n,m)]
    