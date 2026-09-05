# 공던지기
# 한칸씩 건너뜀, 건너뛸때마다 1씩 증가
def solution(numbers, k):
    i = 0
    for _ in range(k-1):
        i = (i+2) % len(numbers)
    return numbers[i]