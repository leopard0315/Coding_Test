# 백준 1946번
# 신입 사원

# 아이디어 : 각 분야 1등은 무조건 포함됨. 2과목 기준으로 정렬
# 따라서 2과목에서 1등이면 1과목에서 타고 내려가다가 1과목 1등까지 도달할때까지 count
# 이때 1과목이 이전 1과목 성적보다 작아야함

# 입력
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    a = []
    # a배열에 요소 추가
    for i in range(N):
        b = list(map(int,input().split()))
        a.append(b)
    # 두번째 요소를 기준으로 정렬
    a.sort(key=lambda x : x[1])
    a_value2 = a[0][0]
    
    # 신입사원 수 세기
    cnt = 1 
    for i in range(1,N):
        if a[i][0] == 1:
            cnt += 1
            break
        if a[i][0] < a_value2:
            a_value2 = a[i][0]
            cnt += 1
        else:
            continue
    # 출력
    print(cnt)
