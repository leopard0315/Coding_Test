# 백준 9226번
# 도깨비말

# 입력
while(1):
    N = input()
    nothing = 0

    # while문 종료조건
    if(N == "#"):
        break
    else:
        # 첫글자가 모음인 경우 -> 끝에 ay 붙이기
        if (N[0] == 'a' or N[0] == 'e' or N[0] == 'i' or N[0] == 'o' or N[0] == 'u'):
            print(N + "ay")
        else :
            # 첫글자를 제외한 모음이 있는 경우
            s = ""
            S = ""
            for i in range(1,len(N)):
                if(N[i] == 'a' or N[i] == 'e' or N[i] == 'i' or N[i] == 'o' or N[i] == 'u'):
                    for j in range(0,i):
                        s += N[j]
                    for j in range(i,len(N)):
                        S += N[j]
                    N = S + s 
                    nothing = 1
                    print(N+"ay")
                    break

            # 단어에 모음이 없을때 -> 단어 끝에 ay 붙이기
            if (nothing == 0):
                print(N+"ay")