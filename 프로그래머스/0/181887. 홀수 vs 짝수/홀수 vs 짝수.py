def solution(num_list):
    sum1 = 0
    sum2 = 0
    for i in range(len(num_list)):
        if i % 2 == 0 :
            sum1 += num_list[i]
        else:
            sum2 += num_list[i]
    
    if sum1 > sum2:
        return sum1
    else:
        return sum2