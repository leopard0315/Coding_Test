# 백준 1316번
# 그룹 단어 체커

# 입력
N = int(input())
count = 0
for _ in range(N):
    cnt = -1
    a = set()
    n = input()
    # 문자열 길이가 1일때
    if (len(n) == 1) :
        cnt = 1
    # 문자열 길이가 2이상일때
    else :
        # 마지막 원소 빼고
        for i in range(len(n)-1):
            if(n[i] != n[i+1]):
                if(n[i] in a): 
                    cnt = 0
                    break
                else:
                    a.add(n[i])
                    cnt = 1
            else:
                continue
        # 마지막 원소 검증
        if(n[-1] in a):
            cnt = 0
        else :
            a.add(n[-1]) 

    if(cnt != 0):
        count += 1

# 출력
print(count)