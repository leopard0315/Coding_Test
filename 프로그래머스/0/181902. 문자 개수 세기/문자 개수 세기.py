def solution(my_string): # 알파벳 대소문자로만 이루어진 문자열 my_string
    answer_A = [0] * 26
    answer_a = [0] * 26

    for i in my_string:
        # 대문자인 경우
        if  ord(i) <= 90:
            answer_A[ord(i)-65] += 1
        # 소문자 인 경우
        elif ord(i) <= 122:
            answer_a[ord(i)-97] += 1
    
    answer_A.extend(answer_a)
    
    return answer_A