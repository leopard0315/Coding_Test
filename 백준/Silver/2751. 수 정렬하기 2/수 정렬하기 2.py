# 백준 2751번
# 수 정렬하기2

import sys
input = sys.stdin.readline

# 입력받기
N = int(input())
a = []

# a배열에 요소 추가
for _ in range(N):
    a.append(int(input()))

# 정렬 - 오름차순
a.sort()

# 출력
print('\n'.join(map(str,a)))