def solution(bridge_length, weight, truck_weights):
    finish = []
    continue_ = []
    timer = 0
    num = len(truck_weights)
    
    while len(finish) < num :
        timer += 1
        con_w = 0
        
        if continue_:
            for i in range(0, len(continue_)):
                if continue_[i][0] == 0:
                    continue
                continue_[i][1] = continue_[i][1] + 1
                if continue_[i][1] > bridge_length:
                    finish.append(continue_[i][0])
                    continue_[i] = [0, 0]
                else:
                    con_w =con_w + continue_[i][0]
            if truck_weights and (con_w + truck_weights[0] <= weight):
                continue_.append([truck_weights.pop(0), 1])
        else:
            if truck_weights:
                continue_.append([truck_weights.pop(0), 1])
                
    return timer