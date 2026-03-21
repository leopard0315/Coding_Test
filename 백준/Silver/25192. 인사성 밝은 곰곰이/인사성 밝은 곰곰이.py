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
        a.clear()
    # 채팅방에 이미 말한 경우
    elif (state in a):
        continue # 여기서는 pass도 가능
    else: # 채팅방에 처음 말한 경우
        a.add(state)
        cnt += 1

# 출력
print(cnt)

# pass : 그냥 문법적으로 채워두는것
# clear은 해당 자료구조를 비울때 사용함