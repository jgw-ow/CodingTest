def solution(s):
    y_value = 0
    p_value = 0
    for i in s.lower():
        if i == 'y':
            y_value += 1
        if i == 'p':
            p_value +=1
    return True if y_value == p_value else False
  