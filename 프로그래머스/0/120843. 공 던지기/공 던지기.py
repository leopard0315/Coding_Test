# 공던지기
# 2칸씩 건너뜀, 건너뛸때마다 1씩 증가
def solution(numbers, k):
    return numbers[ 2* (k-1) % len(numbers)]