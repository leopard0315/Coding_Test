# 회원의 수
N = int(input())
b = []

# 이중 배열 생성
for i in range(N):
    a = []
    age,name = input().split()
    a.append(int(age))
    a.append(name)
    a.append(int(i))
    b.append(a)


# 정렬 - key = lambda 이용 : 첫번째요소 기준으로 정렬 & 두번째 요소를 기준으로 정렬
b.sort(key = lambda x : (x[0], x[2]))
for i in range(len(b)):
    print(b[i][0] , b[i][1])