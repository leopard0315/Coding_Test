def solution(str_list, ex):
    answer = ''
    for i in range (0,len(str_list)):
        if ex in str_list[i]:
            continue
        answer += str_list[i]
    return answer