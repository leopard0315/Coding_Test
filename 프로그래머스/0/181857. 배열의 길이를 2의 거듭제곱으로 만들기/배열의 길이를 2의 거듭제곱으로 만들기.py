def solution(arr):
    # 접근
    # 1. len(arr) < 2**n인 최소 2**n을 찾는다.
    # 2. 2**n-len(arr)번만큼 0을 추가한다.
    
    answer = []
    n = 0
    answer.extend(arr)
   
    while(len(arr) > 2 ** n):
        n += 1
    
    count = 2 ** n - len(arr)
    answer.extend([0] * count)
    
    return answer