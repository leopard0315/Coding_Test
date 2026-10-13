def solution(arr):
    # 접근
    # 1. len(arr) < 2**n인 최소 2**n을 찾는다.
    # 2. 2**n-len(arr)번만큼 0을 추가한다.
    
    # 빈배열과 2의 거듭제곱 정수 n 선언
    answer = []
    n = 0
    
    # answer배열에 arr 요소들만 추가
    answer.extend(arr)
   
    # 2**n이 len(arr)보다 커지는 n값 구하기
    while(len(arr) > 2 ** n):
        n += 1
    
    # 0을 추가하는 횟수를 count값에 저장
    count = 2 ** n - len(arr)
    
    # 0을 count번만큼 추가하기
    answer.extend([0] * count)
    
    # 정답 배열 반환
    return answer