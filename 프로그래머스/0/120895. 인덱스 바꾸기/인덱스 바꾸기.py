def solution(my_string, num1, num2):
    answer = ''
    my_string = list(my_string)
    t = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = t
    return "".join(my_string)