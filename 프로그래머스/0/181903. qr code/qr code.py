def solution(q, r, code):
    # code의 각 인덱스를 q로 나누었을때 나머지가 r인 문자들을 순서대로 이어붙은 문자열 출력
    answer = ''
    
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
            
    return answer