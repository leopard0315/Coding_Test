def solution(my_string, m, c): # 문제를 똑바로 읽자
    answer = ''
    for i in range(c-1,len(my_string),m):
        answer += my_string[i]
    return answer