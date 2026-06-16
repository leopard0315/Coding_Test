def solution(num_list):
    count1 = 0 # 홀수
    count2 = 0 # 짝수
    for i in num_list: # 순서를 쓰는게 아니기때문에 상관없다
        if i%2 == 0 :
            count2 +=1
        else:
            count1 += 1
    answer = [count2,count1]
    return answer