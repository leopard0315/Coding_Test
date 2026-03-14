# 백준 1920번
# 수찾기

import sys
input = sys.stdin.readline

N = int(input())
a = set(map(int,input().split()))
M = int(input())
m = list(map(int,input().split()))

for i in range(len(m)):
    if m[i] in a:
        print(1)
    else:
        print(0)