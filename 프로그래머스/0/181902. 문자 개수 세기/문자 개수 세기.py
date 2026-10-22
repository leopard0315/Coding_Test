# 접근: 대문자의 개수 모은 배열 + 소문자의 개수 모은 배열을 합쳐서 최종 결과를 반환한다.
def solution(my_string): # 알파벳 대소문자로만 이루어진 문자열 my_string
    answer_A = [0] * 26 # 대문자만 모아둔 배열
    answer_a = [0] * 26 # 소문자만 모아둔 배열

    for i in my_string:
        # 대문자인 경우
        if  ord(i) <= 90:
            answer_A[ord(i)-65] += 1
        # 소문자 인 경우
        elif ord(i) <= 122:
            answer_a[ord(i)-97] += 1
    
    # 대문자 개수 배열에다가 소문자 개수 배열 합치기
    answer_A.extend(answer_a)
    
    # 최종 정답 반환
    return answer_A