# 백준 - 18247번

# testcase 개수
T = int(input())
for _ in range(T):
    # N:세로(행 개수) / M:가로(열 개수)
    N,M = map(int,input().split())
    # 예외처리
    if(N < 12 or M < 4):
        print(-1)
    else:
        # 좌석번호 계산
        seat_num = 11 * M + 4
        print(seat_num)