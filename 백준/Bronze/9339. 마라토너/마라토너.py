# 백준 9339번
# 마라토너

# 입력
# 테스트 케이스 개수
T = int(input())

# 방법1 - 필요한 값만 사용해서 구하기
for j in range(T):
    # 수강생의 수
    K = int(input())
    # 수강생의 참가번호 리스트
    a = list(map(int,input().split()))
    # 대회 참가자 수
    N = int(input())

    # 대회 참가자 수에서 인증서를 받은 수강생들만 모은 배열
    b = []
    min = 361
    # 인증서를 받은 수강생들의 수세기
    count = 0

    for _ in range(N):
        num,hour,minute = map(int,input().split())
        time = hour * 60 + minute

        # 6시간 이하이고 -1이 아닐때 추가
        if(time < 361 and time != -61 and num in a):
            if(time < min):
                min = time
                best_num = num
            count += 1
    # 가장 기록이 좋은 수강생의 번호 , 인증서를 받은 수강생의 수
    print(best_num,count)

# # 방법2 - 혹시 모르니 새로운 배열을 생성해서 필요한 값외의 정보들을 모두 포함해서 정렬한후에 필요한 부분만 발췌하기
# for j in range(T):
#     # 수강생의 수
#     K = int(input())
#     # 수강생의 참가번호 리스트
#     a = list(map(int,input().split()))
#     # 대회 참가자 수
#     N = int(input())

#     # 대회 참가자 수에서 인증서를 받은 수강생들만 모은 배열
#     b = []

#     for _ in range(N):
#         B = list(map(int,input().split()))
#         for i in range(len(a)):
#             if(a[i] == B[0]):
#                 # 6시간 이하이고 -1이 아닐때 추가
#                 if(B[1] <= 5 and B[1] != -1):
#                     b.append(B)
#                 elif(B[1] == 6 and B[2] == 0):
#                     b.append(B)
#                 break
#             else:
#                 continue

#     # 구해야할 것 : 가장 기록이 좋은 수강생의 번호, 인증서를 받은 수강생의 수

#     # 정렬 (시/분이 빠른 순서대로 정렬)
#     b.sort(key = lambda x : (x[1], x[2]))
#     print(b[0][0],len(b))