def solution(my_string):
    answer = []
    my_string_list = my_string.split(' + ')
    for i in my_string_list:
        total = 0
        # i 가 3 - 4 인경우
        if '-' in i:
            l = i.split(' - ')
            total = int(l[0])
            for k in range(1,len(l)):
                total -= int(l[k])
        # i가 3 그냥 숫자인경우
        else:
            total = int(i)

        answer.append(total)

    ans = 0 
    for j in range(len(answer)):
        ans += answer[j]
    return ans