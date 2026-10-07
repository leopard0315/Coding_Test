def solution(num_list):
    count = 0
    # num_list 배열 안에 요소중들중에
    # 홀수인지 짝수인지 판별하고 결과값이 1인지 아닌지 판단
    for i in num_list:
        while(i != 1):
            if i % 2 == 0:
                i = i // 2
            else:
                i = (i - 1) // 2
            count += 1
    return count