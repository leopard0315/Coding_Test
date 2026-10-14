# 약수가 3개이상인 수: 합성수 -> 소수가 아닌 수
def solution(n):
    answer = 0 # 합성수의 개수
    count = 0 # 약수의 개수가 3개이상인지 파악
    
    # n이하의 원소 1개 뽑기(i)
    for i in range(1,n+1):
        # 뽑은 원소 i의 약수가 3개이상인지 확인하기위해
        # i이하의 원소들을 전부뽑아서 약수가 되는지 확인
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
            else:
                continue
                
        # 약수의 개수가 3개이상이면 합성수 -> answer 값 1 증가        
        if count >= 3:
            answer += 1
        
        # 약수의 개수 0으로 다시 초기화
        count = 0
    
    # 합성수의 개수 반환하기
    return answer
                