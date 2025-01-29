def solution(arr):
    X = []
    for i in arr:
        for j in range(0, i):
            X.append(i)
    return X