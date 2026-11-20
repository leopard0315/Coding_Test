def solution(n):
    answer = 0
    # 여기까지는 1부터 절반 값까지만
    for i in range(1,n//2+1):
        if n % i == 0:
            answer += i
    # 마지막 본인까지 포함하기
    return answer + n