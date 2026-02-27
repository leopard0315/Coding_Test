# 백준 11478번
# 서로 다른 부분 문자열의 개수

# 입력
S = input()
A = set()
i = 0

# 문자열의 개수 계산
while(1):
    for j in range(len(S)-i):
        A.add(S[j:j+(i+1)])
    i += 1
    if(i == len(S)):
        break

# 출력
print(len(A))