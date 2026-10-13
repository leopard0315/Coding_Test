# 약수가 3개이상인 수: 합성수 -> 소수가 아닌 수
def solution(n):
    answer = 0 # 합성수의 개수
    count = 0 # 약수의 개수가 3개이상인지 파악
    
    for i in range(1,n+1): # n번 반복
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
            else:
                continue
                
        if count >= 3:
            answer += 1
            
        count = 0
            
    return answer
                