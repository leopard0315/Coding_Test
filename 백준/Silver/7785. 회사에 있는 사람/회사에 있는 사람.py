# 백준 7785번
# 회사에 있는 사람
# 로그 -> 현재 회사에 있는 모든 사람 구하기

# 입력
n = int(input())
name = set()
cnt = 0

for _ in range(n):
    n, l = map(str,input().split())
    # 출근을 했을때
    if (n in name):
        name.remove(n)
        cnt -= 1
    # 출근을 안했을때
    else:
        name.add(n)
        cnt += 1

# 사전 역순으로 출력
dictionary = sorted(name, reverse = True)
print(*dictionary,sep ='\n')