def solution(array):
    index = 0
    for i in range(len(array)):
        if array[i] == sorted(array)[-1]:
            index += i
    return [sorted(array)[-1], index]