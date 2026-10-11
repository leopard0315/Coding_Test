def solution(board, k): # board 이차원 배열, 정수 k
    answer = 0
    # i + j <= k인지 확인, 아니면 다음 반복문으로 이동
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i + j) <= k:
                answer += board[i][j]
            else:
                continue
    return answer