# def solution(arr):
#     answer = []
#     for i in range(0, len(arr)-1):
#         if arr[i] != arr[i+1]:
#             answer.append(arr[i])
#     answer.append(arr[-1])
#     return answer

def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer