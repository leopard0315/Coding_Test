def solution(numbers):
    # - 를 유의하기
    numbers.sort() # 오름차순 정렬
    a1 = numbers[-1] * numbers[-2]
    a2 = numbers[0] * numbers[1]
    return max(a1,a2)