def solution(my_string, s, e):
#     # 제한사항 0 <= s <= e < len(my_string) 
#     # 반례: s가 0인 경우 -> my_string[:s]랑 my_string[e:s-1:-1]가 출력되지 않는다.
    
#     # s가 0인 경우
#     # my_string[0]을 추가해준다.
#     if s == 0:
#         return my_string[e:0:-1] + my_string[0] + my_string[e+1:]
#     # s가 0이 아닌 경우
#     # s전까지 자른거 + s~e까지 뒤집은 문자열 + e이후 문자열을 모두 더한 문자열 출력
#     else:
#         return my_string[:s] + my_string[e:s-1:-1] + my_string[e+1:]
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]