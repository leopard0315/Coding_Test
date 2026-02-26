# 백준 11383번
# 뚊

# 입력
N, M = map(int,input().split())
A = []
B = []
str1 = ""
cnt = 0

# 첫번째 이미지
for _ in range(N):
    a = input()
    for i in range(len(a)):
        str1 = str1 + a[i] * 2
    A.append(str1)
    str1 = ""
# 두번째 이미지
for i in range(N):
    b = input()
    if(A[i] == b):
        continue
    else:
        cnt = 1

# 출력
if(cnt != 1):
    print("Eyfa")
else:
    print("Not Eyfa")