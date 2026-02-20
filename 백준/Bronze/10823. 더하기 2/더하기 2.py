# 백준 10823번
# 더하기 2

# 입력하는대로 그냥 문자열을 다 받음
import sys
s = sys.stdin.read()

# replace(A,B).split(',') -> A를 B로 바꾸고 ,를 기준으로 나누어라
data = list(map(int,s.replace('\n','').split(',')))

print(sum(data))