def solution(rny_string):
    rny_string = list(rny_string) # 파이썬에서는 문자열은 불변이기 때문에 list로 변환하여 사용한다.
    
    for i in range(len(rny_string)): # 문자열 변경
        if rny_string[i] == 'm':
            rny_string[i] ='rn'
             
    answer = "".join(rny_string) # 문자열 합치기
    
    return answer # 반환값 반환하기