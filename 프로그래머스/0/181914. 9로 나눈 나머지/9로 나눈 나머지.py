def solution(number):
    # number는 문자열 type
    
    # # 1. 음이 아닌 정수를 9로 나눈 나머지 구하기
    # answer = int(number) % 9
    # return answer
    
    # 2. 정수의 각 자리의 숫자의 합 구하기
    total = 0
    for i in number:
        total += int(i)
    return total % 9