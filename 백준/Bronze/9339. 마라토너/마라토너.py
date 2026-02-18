# 백준 9339번
# 마라토너

# 입력
# 테스트 케이스 개수
T = int(input())

for j in range(T):
    # 수강생의 수
    K = int(input())
    # 수강생의 참가번호 리스트
    a = list(map(int,input().split()))
    # 대회 참가자 수
    N = int(input())

    # 대회 참가자 수에서 인증서를 받은 수강생들만 모은 배열
    b = []

    for _ in range(N):
        B = list(map(int,input().split()))
        for i in range(len(a)):
            if(a[i] == B[0]):
                # 6시간 이하이고 -1이 아닐때 추가
                if(B[1] <= 5 and B[1] != -1):
                    b.append(B)
                elif(B[1] == 6 and B[2] == 0):
                    b.append(B)
                break
            else:
                continue

    # 구해야할 것 : 가장 기록이 좋은 수강생의 번호, 인증서를 받은 수강생의 수

    # 정렬 (시/분이 빠른 순서대로 정렬)
    b.sort(key = lambda x : (x[1], x[2]))
    print(b[0][0],len(b))