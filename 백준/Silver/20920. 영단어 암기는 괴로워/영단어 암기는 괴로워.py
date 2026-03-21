# 백준 20920번
# 영단어 암기는 괴로워
import sys
input = sys.stdin.readline
from collections import Counter

# 입력
N,M = map(int,input().strip().split())
a = []
for i in range(N):
    word = input().strip()
    if len(word) < M:
        pass
    else: # 단어의 길이가 M보다 크거나 같으면 추가
        a.append(word)

# 단어 횟수 count하기
word_count = Counter(a)
word_cnt = list(word_count.items())

# 정렬 3가지 기준 정렬 : -x[1]은 단어나온횟수를 기준으로, len(x[0])은 단어의 길이를 기준으로, x[0]은 단어 사전순으로 
word_cnt.sort(key= lambda x : (-x[1],-len(x[0]),x[0]))

# 출력
for word,cnt in word_cnt:
    print(word)