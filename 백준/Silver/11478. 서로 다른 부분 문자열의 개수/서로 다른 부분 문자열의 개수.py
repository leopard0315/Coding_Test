# 백준 11478번
# 서로 다른 부분 문자열의 개수

# 입력
S = input()
A = []
i = 0

# 문자열을 A배열의 추가
while(1):
    for j in range(len(S)-i):
        A.append(S[j:j+(i+1)])
    i += 1
    if(i == len(S)):
        break

# 서로 다른 문자열의 개수 출력
a = set(A)
print(len(a))