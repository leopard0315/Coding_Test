# 최대공약수를 찾는 함수 gcd & 라이브러리 math이용
# import math
# math.gcd(a,b)

# a와 b의 최소공배수 : a * b // gcd(최대공약수) -> 최대공약수는 둘이 겹치는 부분이기때문에 겹치는 부분 한번만 곱해지도록 나누어준다. 
import math
def solution(numer1, denom1, numer2, denom2):
    n =  numer1 * denom2 + numer2 * denom1 # 분자
    d = denom1  * denom2    # 분모
    
    # 최대공약수 구하기 - gcd()이용
    g = math.gcd(n,d)
        
    # 정답 반환
    return [n//g, d//g]