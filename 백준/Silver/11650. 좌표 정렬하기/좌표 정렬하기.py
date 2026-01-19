# 점의 개수
N = int(input())

# 이중 배열 생성
a = [list(map(int,input().split())) for i in range(N)]

# 정렬 - key = lambda 이용 : 첫번째요소 기준으로 정렬 & 두번째 요소를 기준으로 정렬
a.sort(key = lambda x : (x[0],x[1]))
for i in range(len(a)):
    print(a[i][0] , a[i][1])