def solution(my_string, target):
    answer = 0
    length = len(target)
    for i in range(0,len(my_string)):
        if(my_string[i:i+len(target)] == target):
            answer = 1
            break
        else:
            continue
    return answer