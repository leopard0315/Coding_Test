# 백준 2292번
# 벌집

# 입력 & 변수 선언
N = int(input())
i = 1
room = 1

# 벌집의 방이 N 개 방보다 큰 경우 종료
while N > room:
    # 벌집 규칙
    room += 6* i
    i += 1
print(i)