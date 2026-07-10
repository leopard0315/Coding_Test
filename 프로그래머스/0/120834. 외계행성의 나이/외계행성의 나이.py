def solution(age):
    answer = ''
    while(age != 0):
        num = age % 10 # 숫자 1개
        print(age)
        if num == 0 :
            answer = 'a' + answer
        elif num == 1:
            answer = 'b' + answer
        elif num == 2:
            answer = 'c' + answer
        elif num == 3:
            answer = 'd' + answer
        elif num == 4:
            answer = 'e' + answer
        elif num == 5:
            answer = 'f' + answer
        elif num == 6:
            answer = 'g' + answer
        elif num == 7:
            answer = 'h' + answer
        elif num == 8:
            answer = 'i' + answer
        elif num == 9:
            answer = 'j' + answer
            
        age = age // 10
        
    return answer