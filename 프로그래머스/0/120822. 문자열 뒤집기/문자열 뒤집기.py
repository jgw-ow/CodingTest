def solution(my_string):
    reverse = my_string[::-1]
    answer = ''
    for i in range(len(my_string)):
        answer += reverse[i]
    return answer
        