def solution(my_string, m, c):
    answer = ''
    start = m * (c-1)
    for i in range(c-1,len(my_string),m):
        answer += my_string[i]
    return answer