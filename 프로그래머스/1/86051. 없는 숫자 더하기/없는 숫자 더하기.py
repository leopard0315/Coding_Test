def solution(numbers):
    # 풀이1
    # num = [0,1,2,3,4,5,6,7,8,9]
    # total = 0
    # for i in num:
    #     if i not in numbers:
    #         total += int(i)
    # return total

    # 풀이2
    return 45 - sum(numbers)