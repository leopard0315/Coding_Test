# 열순서
# 26년 4월 10일

c = input()
result = 0
for ch in c:
    result = result * 26 + (ord(ch) - 64)
print(result)    