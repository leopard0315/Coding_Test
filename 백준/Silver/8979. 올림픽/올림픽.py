# 1월 19일
# 8979번 - 백준
N, K = map(int,input().split())

# 입력할 이중 배열 생성
medals = [list(map(int,input().split())) for _ in range(N)]

# 생성한 이중배열을 첫번째요소-두번째요소-세번째 요소에 따라서 정렬한다.
# key = lambda를 활용해서 해결할 수 있다.
# sort(key = lambda x : (x[1],x[2],x[3]) , reverse = True)
# 여기서 이미 정렬이 되어있는 상태이다.
medals.sort(key = lambda x : (x[1],x[2],x[3]),reverse = True)

# K에 해당하는 인덱스를 찾아서 idx에 저장한다.
idx = [medals[i][0] for i in range(N)].index(K)

for i in range(N):
    if(medals[idx][1:] == medals[i][1:]):
        print(i+1)
        break