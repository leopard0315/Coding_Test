def solution(my_strings, parts):
    # 정답을 담을 변수 선언
    answer = ''
    # my_strings을 각 넘버링 해주는 문자열
    i = 0
    
    # parts의 원소를 s,e로 뽑아내서 my_strings의 각 원소들을 문자열 슬라이싱을 이용해서 잘라냄
    for s,e in parts:
        answer += my_strings[i][s:e+1]
        i += 1
        
    # 정답 반환
    return answer