def solution(my_string):
    answer = ''
    for i in my_string: # 문자열안에 각 문자가 
        if i not in answer: # answer안에 없을때 추가한다.
            answer += i
    return answer
    