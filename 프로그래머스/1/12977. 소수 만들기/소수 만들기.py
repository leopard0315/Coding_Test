from itertools import combinations
def solution(nums):
    c = list(combinations(nums,3))
    total_list = []
    for i in c:
        sum_num = sum(list(i))
        total_list.append(sum_num)
    
    count = 0
    # total_list에서 원소뽑아서 그 소수인지 확인하기
    for i in range(len(total_list)):
        count += 1
        for j in range(2,total_list[i]//2 +1):
            if total_list[i] % j == 0:
                count -= 1
                break
    return count