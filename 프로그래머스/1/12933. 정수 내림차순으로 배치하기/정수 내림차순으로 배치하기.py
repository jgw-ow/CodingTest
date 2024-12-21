def solution(n):
    answer1 = []
    answer2 = ''
    for i in str(n):
        answer1 += i
    for j in sorted(answer1, reverse = True):
        answer2 += j
    return int(answer2)
    