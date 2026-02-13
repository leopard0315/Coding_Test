# 백준 10809번
# 알파벳 찾기

# 입력
S = input()
s = list(S) # 배열화

# 배열 2개 생성
b = []
num = 97
for i in range(26):
    b.append(int(num + i))

c = [-1] * 26

# 위치 출력
for i in range(len(s)):
    for j in range(len(b)):
        if(ord(s[i]) == b[j]):
            # 중복인 경우(이미 -1이 아님)
            if(c[j] != -1):
                continue
            # 중복이 아닌 경우
            else:
                c[j] = i
            break
print(*c)