A, B, C = map(int, input().split())
D = int(input())

# 모두 초 단위로 변환
total_seconds = A * 3600 + B * 60 + C + D

# 하루(24시간) = 86400초 이므로 나머지 연산으로 24시간 기준 유지
total_seconds %= 86400

# 다시 시, 분, 초로 분해
A = total_seconds // 3600
B = (total_seconds % 3600) // 60
C = total_seconds % 60

print(A, B, C)
