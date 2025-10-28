T = int(input()) # 테스트케이스 개수
for i in range(T): # 각 테스트케이스 별로 수행
    N = input()
    sum = 0
    score = 0
    for j in range(0,len(N)): # 테스트케이스의 문자열 길이만큼 수행
        if(N[j] == "O"): 
            score += 1 # 점수 누적 진행 -> X가 나올때까지 계속 점수 누적
            sum += score
        else: # X일때 score가 0으로 초기화됨
            score = 0
    print(sum)