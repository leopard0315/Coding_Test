def solution(my_string):
    answer = []
    my_string_list = my_string.split(' ')
    print(my_string_list)
    
    for i in my_string_list:
        if i != '':
            answer.append(i)
    
    return answer