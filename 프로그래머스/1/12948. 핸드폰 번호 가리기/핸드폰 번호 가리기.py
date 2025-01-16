def solution(num):
    num_list = list(num)
    for i in range(len(num_list[:-4])):
        num_list[i] = "*"
    return ''.join(num_list)