# 백준 1941번
# 크로아티아 알파벳

# 입력
word = list(map(str,input()))
cnt = 0
i = 0

# case별로 나누기
while i < len(word):
    # 시작이 c인 경우
    if(word[i] == 'c'):
        if(i+1 < len(word))and(word[i+1] == '=' or word[i+1] == '-'):
            i += 1
        cnt += 1
    # 시작이 d인 경우
    elif(word[i] == 'd'):
        if(i+2 < len(word))and (word[i+1] == 'z' and word[i+2] == '='):
            i += 2
        elif(i+1 < len(word))and(word[i+1] == '-'):
            i += 1
        cnt += 1
    # lj인 경우
    elif(word[i] == 'l'):
        if(i+1 < len(word))and(word[i+1] == 'j'):
            i += 1
        cnt += 1
    # nj인 경우
    elif(word[i] == 'n'):
        if(i+1 < len(word))and (word[i+1] == 'j'):
            i += 1
        cnt += 1
    # s=인 경우
    elif(word[i] == 's'):
        if(i+1 < len(word))and (word[i+1] == '='):
            i += 1
        cnt += 1
    # z=인 경우
    elif(word[i] == 'z'):
        if(i+1 < len(word))and (word[i+1] == '='):
            i += 1
        cnt += 1
    # 그외의 알파벳이 올때
    else:
        cnt += 1
    
    i += 1

# 출력
print(cnt)

# for문 : 루프 시작시 순회할 대상이 고정된다. 내부에서 변수를 변경해도 무시됨
# while문 : 조건을 매번 평가하기 때문에 가변적 조건에 어울린다.