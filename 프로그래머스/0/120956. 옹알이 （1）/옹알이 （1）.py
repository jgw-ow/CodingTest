# def solution(babbling):
#     arr = ["aya", "ye", "woo", "ma"]
#     arr_last = ["aya", "ye", "woo", "ma"]
#     count = 0
#     for i in arr:
#         for j in arr:
#             if i != j:
#                 arr_last += [i+j]
#                 for k in arr:
#                     if j != k and i != k:
#                         arr_last += [i+j+k]
#                         for l in arr:
#                             if k != l and j != l and i != l:
#                                 arr_last += [i+j+k+l]
#     for n in babbling:
#         if n in arr_last:
#             count += 1
#     return count
def solution(babbling):
    valid_words = {"aya", "ye", "woo", "ma"}  # 발음할 수 있는 단어들
    count = 0  # 발음 가능한 단어 개수
    
    for word in babbling:
        temp = word
        for v in valid_words:
            temp = temp.replace(v, " ")  # 발음 가능한 단어들을 공백으로 변환
        if temp.strip() == "":  # 공백만 남아있다면, 유효한 단어
            count += 1

    return count
