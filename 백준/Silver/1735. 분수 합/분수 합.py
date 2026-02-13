# 백준 1735번
# 분수 합

import math

# 입력
A,B = map(int,input().split())
C,D = map(int,input().split())

# 분모 계산
denominator = B * D

# 분자 계산
numerator = A * D + B * C

# 기약 분수 형태로 최대공약수 제거
same = math.gcd(denominator,numerator)

# 출력
print(numerator // same, denominator // same)