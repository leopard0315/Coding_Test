import math
def solution(numer1, denom1, numer2, denom2):
    answer = []  # 첫번째: 분자, 두번째: 분모
    n =  numer1 * denom2 + numer2 * denom1 # 분자
    d = denom1  * denom2    # 분모
    
    g = math.gcd(n,d)
    
    answer.append(n//g)
    answer.append(d//g)
        
    
    return answer