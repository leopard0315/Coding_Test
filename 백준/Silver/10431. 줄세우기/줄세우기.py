# 백준 10431번
# 줄세우기

# 입력
P = int(input())

for _ in range(P):
    walk_cnt = 0
    a = list(map(int,input().split()))
    b = [a[0],a[1]]

    for i in range(2,21):
        for j in range(1,i+1):
            if(a[j] > a[i]):
                # 배열에 특정 위치에 요소를 추가할때 -> insert(위치, 요소) 를 사용
                b.insert(1,a[i])
                walk_cnt += 1

    # 출력
    print(a[0], walk_cnt)