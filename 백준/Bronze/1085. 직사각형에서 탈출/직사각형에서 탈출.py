# 백준 1085번
# 직사각형에서 탈출

# 입력
x,y,w,h = map(int,input().split())

# 각 점에서 변으로 수선의 발을 내린것이 거리의 최솟값
# 경우의 수 : 4가지 이므로 이중에서 최소값을 찾으면 됨
a = []
a.append(int(x))
a.append(int(y))
a.append(int(h-y))
a.append(int(w-x))

# 거리 최소 순서대로 정렬
a.sort()

# 출력
print(a[0])