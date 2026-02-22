# 백준 25372번
# 성택이의 은밀한 비밀번호

# 입력
N = int(input())
for _ in range(N):
    n = input()
    if(len(n) >= 6 and len(n) <= 9):
        print("yes")
    else:
        print("no")