# 백준 20920번
# 영단어 암기는 어려워
# 아이디어 : 한 배열을 만들어서 count값과 길이 알파벳 사전순으로 되도록 순서대로 한다.

from collections import Counter
import sys
input = sys.stdin.readline

# 입력
N,M = map(int,input().strip().split())
A = []
for i in range(N):
    n = input().strip()
    if len(n) < M :
        continue
    else: # 단어의 길이가 M이상인 경우
        A.append(n)

# Counter사용해서 횟수 카운트하기
word_cnt = Counter(A)
word_set = list(word_cnt.items())

# 정렬기준 3가지 / - : desc, + : asc
word_set.sort(key = lambda x: (-x[1],-len(x[0]),x[0]))

# 출력
for word,cnt in word_set:
    print(word)