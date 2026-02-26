# 백준 27110번
# 특식 배부

# 입력
N = int(input())
cnt = 0

# 최대인원수 계산
ABC = list(map(int,input().split()))
for i in range(3):
    if(ABC[i] >= N):
        cnt += N
    else:
        cnt += ABC[i]

# 출력
print(cnt)