# 백준 1931번
# 회의실 배정

# 입력
N = int(input())
conf = []
for _ in range(N):
    c = list(map(int,input().split()))
    conf.append(c)

# 회의실 끝나는 시간 기준으로 정렬(두번째 요소 기준 정렬)
# 오름차순 : + , 내림차순 : -
conf.sort(key = lambda x : (x[1], x[0]))

# 회의 최대개수 구하기
cnt = 1
k = 0
a = [conf[0][1]]
while(True):
    for i in range(k+1,N):
        if(conf[k][1] <= conf[i][0]):
            cnt += 1
            k = i
    break
print(cnt)