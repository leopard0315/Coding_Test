# 백준 9012번
# 괄호

# 입력
N = int(input())

for _ in range(N):
    a = []
    count = 0
    n = input()
    for i in range(len(n)):
        if n[i] == "(":
            a.append(n[i])
        elif n[i] == ")":
            if len(a) == 0:
                count = 1
                break
            a.pop()
    if (count == 1 or len(a) != 0):
        print("NO")
    else:
        print("YES")