def solution(my_string, s, e):
    if s == 0:
        answer = my_string[e:0:-1] + my_string[0] + my_string[e+1:]
    else:
        answer = my_string[:s] + my_string[e:s-1:-1] + my_string[e+1:]
    # print(my_string[:s])
    # print(my_string[e:s-1:-1])
    # print(my_string[e+1:])
    return answer