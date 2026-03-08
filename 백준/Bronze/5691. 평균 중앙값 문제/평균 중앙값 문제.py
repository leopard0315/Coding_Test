# 백준 5691번
# 평균 중앙값 문제

# 경우의 수는 3가지 (A,B,C) or (A,C,B) or (C,A,B)

while(1):
    A,B = map(int,input().split())

    # while문 종료조건
    if(A == 0 or B == 0):
        break
    else:
        C = 2 * A - B
        print(C) 