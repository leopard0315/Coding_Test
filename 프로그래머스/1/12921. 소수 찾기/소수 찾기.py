# 에라토스테네스의 체
# 처음에 모두 1인 배열 생성
# 만약 해당 원소가 배열이 소수라면 소수에 해당하는 배수들을 전부 제거
# 맨 마지막에 1로 남아있는게 소수라는 소리
import math

def solution(n):
    prime = [True for i in range(n+1)]
    
    for i in range(2, int(math.sqrt(n))+1):
        if prime[i] == True:
            j = 2
            while i * j <= n:
                prime[i*j] = False
                j += 1
    return prime.count(True) -2
    