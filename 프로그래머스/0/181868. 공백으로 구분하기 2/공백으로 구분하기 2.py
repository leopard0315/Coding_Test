def solution(my_string):
    # 1. 빈배열 생성
    answer = []
    
    # 2. 공백을 기준으로 문자열을 쪼갠다.
    my_string_list = my_string.split(' ')
    
    # 3. 만약 빈 공백이 아니라면 배열에 추가한다.
    for i in my_string_list:
        if i != '':
            answer.append(i)
    
    # 4. 정답 배열 반환
    return answer