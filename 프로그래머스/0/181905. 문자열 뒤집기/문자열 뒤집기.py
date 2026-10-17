def solution(my_string, s, e):
    # 제한사항 0 <= s <= e < len(my_string) 
    # 반례: s가 0인 경우 -> my_string[:s]랑 my_string[e:s-1:-1]가 출력되지 않는다.
    
    # s가 0인 경우 / s가 0이 아닌 경우로 나눈다.
    if s == 0:
        return my_string[e:0:-1] + my_string[0] + my_string[e+1:]
    else:
        return my_string[:s] + my_string[e:s-1:-1] + my_string[e+1:]