# 백준 25192번
# 인사성 밝은 곰곰이
# 목표 : 채팅방의 기록을 통해 곰곰티콘이 사용된 횟수 구하기
import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
a = set()
cnt = 0

for i in range(N):
    state = input().strip()

    # 채팅방에 누군가 들어왔을때
    if state == "ENTER":
        a = set()
    else:
        # 채팅방에 이미 말한 경우
        if state in a:
            continue
        else: # 채팅방에 처음 말한 경우
            a.add(state)
            cnt += 1

# 출력
print(cnt)