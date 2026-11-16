def solution(num):
    # 단, 주어진 수가 1 -> 0 반환, 작업을 500번 반복할때까지 1이 되지 않는다면, -1 반환하기
    if num == 1:
        return 0
    
    count = 0
    for i in range(500):
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        count += 1
        if num == 1:
            return count
    return -1