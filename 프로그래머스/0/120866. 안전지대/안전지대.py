def solution(board):
    n = len(board)
    padding = [[0] * (n+2) for i in range(n+2)]
    print(padding)

    for i in range(n):
        for j in range(n):
            padding[i+1][j+1] = board[i][j]

    print(padding)
    safe = 0

    for i in range(1,n+1):
        for j in range(1,n+1):
            # 해당 원소가 지뢰인경우
            if padding[i][j] == 1:
                continue
            # 해당 원소 주변에 지뢰가 있는 경우
            if padding[i][j+1] == 0 and padding[i][j-1] == 0 and padding[i-1][j] == 0 and padding[i+1][j] == 0 and padding[i-1][j+1] == 0 and padding[i-1][j-1] == 0 and padding[i+1][j-1]==0 and padding[i+1][j+1] == 0:
                safe += 1
    return safe