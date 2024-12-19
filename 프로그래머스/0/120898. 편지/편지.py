def solution(message):
    answer = 0
    for i in range(1, len(message)+1):
        answer += 2
    return answer
