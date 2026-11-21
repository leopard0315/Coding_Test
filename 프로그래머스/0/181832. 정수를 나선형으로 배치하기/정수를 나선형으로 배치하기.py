def solution(n):
    arr = [[0] * n for i in range(n)]
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    num , x, y, d = 1, 0, 0, 0 # num은 원소의 개수 count, x,y는 위치 표시, d는 방향
    while(num <= n**2):
        arr[x][y] = num
        num += 1
        
        # 다음꺼 적용시
        nx ,ny = x + direction[d][0] , y + direction[d][1]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] != 0:
            d = (d+1) % 4
            nx ,ny = x + direction[d][0] , y + direction[d][1]
        
        # 값 재할당
        x,y = nx, ny
        
    return arr