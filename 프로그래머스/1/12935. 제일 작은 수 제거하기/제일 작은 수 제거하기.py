def solution(arr):
    if len(arr) == 1:
        return [-1]
    min_arr = min(arr)
    arr.remove(min_arr)
    return arr
