from collections import Counter

# 3985번 백준
L = int(input()) # 롤 케이크의 길이
List = [0 for i in range(L)]

# 예상 리스트 번호
a  = []

count = 0
N = int(input()) # 방청객 번호
for j in range(1,N+1):
    P,K = map(int,input().split())
    a.append(int(K-P))
    for i in range(P,K+1): # P < K
        if(List[i-1] == 0):
            List[i-1] = j
        else :
            continue

# 예상 리스트의 번호        
print(a.index(max(a))+1)

# 실제 방청객의 번호
count_items = Counter(List)
max_item = count_items.most_common()

if(max_item[0][0] == 0):
    print(max_item[1][0])
else:
    print(max_item[0][0])