# 백준 26069번
# 붙임성 좋은 총총이

# 입력
N = int(input())
meet_list = ["ChongChong"]

# 계산
for _ in range(N):
    p1, p2 = map(str,input().split())
    # 만나는 경우(첫번째 사람)
    if(p1 in meet_list):
        if(p2 not in meet_list):
            meet_list.append(p2)
    # 만나는 경우(두번째 사람)
    elif(p2 in meet_list):
        if(p1 not in meet_list):
            meet_list.append(p1)
    # 만나지 않는 경우
    else:
        continue

# 출력
print(len(meet_list))