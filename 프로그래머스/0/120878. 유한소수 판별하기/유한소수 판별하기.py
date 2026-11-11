import math
def solution(a, b):
    # 최대 공약수 구하기
    Gcd = math.gcd(a,b)
    
    # 기약 분수로 표현
    b = b // Gcd
    
    # 분모의 소인수 2와 5만 존재하는지 확인
    while(b % 5 == 0):
        b = b // 5
    while(b % 2 == 0):
        b = b // 2
    
    # 분모가 2로 나누고, 5로 나눈 이후에는 분모가 1이어야 유한소수/ 아니라면 무한 소수
    if b != 1:
        return 2
    else:
        return 1