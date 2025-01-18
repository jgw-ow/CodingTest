def solution(babbling):
    arr = ["aya", "ye", "woo", "ma"]
    arr_last = ["aya", "ye", "woo", "ma"]
    count = 0
    for i in arr:
        for j in arr:
            if i != j:
                arr_last += [i+j]
                for k in arr:
                    if j != k and i != k:
                        arr_last += [i+j+k]
                        for l in arr:
                            if k != l and j != l and i != l:
                                arr_last += [i+j+k+l]
    for n in babbling:
        if n in arr_last:
            count += 1
    return count