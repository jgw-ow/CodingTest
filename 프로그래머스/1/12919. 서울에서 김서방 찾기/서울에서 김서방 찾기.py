def solution(seoul):
    answer = 0
    for x in range(0, len(seoul)):
        if seoul[x] == 'Kim':
            return f"김서방은 {x}에 있다"