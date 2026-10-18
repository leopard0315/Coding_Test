def solution(my_string):
    total = 0
    for i in range(len(my_string)):
        if my_string[i].isalpha():
            my_string = my_string.replace(my_string[i],' ')
    
    my_string_list = my_string.split()
    for i in my_string_list:
        total += int(i)
        
    return total
    