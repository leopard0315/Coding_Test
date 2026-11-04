def solution(numbers):
    # 방법3 - enumerate함수 사용
    for num,eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng,str(num))    
    return int(numbers)
    
    # 방법2 - dictionary 이용
    # dict = {'zero': 0,'one': 1,'two': 2,'three': 3,'four': 4,
    #         'five': 5,'six': 6,'seven': 7,'eight': 8, 'nine': 9}
    # for i in dict.keys():
    #     numbers = numbers.replace(i,str(dict[i]))
    # return int(numbers)
    
    # 방법1 - 전부 replace()이용
    # num = numbers.replace('zero','0').replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9')
    # return int(num)
    