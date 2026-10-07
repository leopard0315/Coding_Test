def solution(n):
    # 1. n x n크기의 2차원 배열 생성(모든 원소 0)
    answer = [[0 for j in range(n)] for i in range(n)]
    
    # 2. arr[i][j], i==j인 경우에 1 else 0
    for i in range(n):
        for j in range(n):
            if i == j:
                answer[i][j] = 1
            else:
                continue
    return answer