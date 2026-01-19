# 수의 개수 입력
N = int(input())
a = []

# 입력받은 수에 값을 a 배열에 저장
for i in range(N):
    n = int(input())
    a.append(int(n))

# 오름차순 정렬 진행
a.sort()

# 출력 진행
for i in range(len(a)):
    print(a[i])
