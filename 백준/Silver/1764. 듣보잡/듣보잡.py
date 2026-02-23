# 백준 1764번
# 듣보잡

# 입력
N, M = map(int,input().split())
n = set()
intersection = set()

for i in range(N):
    name = input()
    n.add(name)
for j in range(M):
    name = input()
    if name in n :
        intersection.add(name)

# set->list변경 & 사전순 정렬
inter_list = list(intersection)
inter_list.sort()

# 출력
print(len(inter_list))
print(*inter_list, sep = '\n')