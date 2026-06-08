def solution(myString):
    myString1 = list(map(str,myString.split('x')))
    answer = []
    for i in range(len(myString1)):
        answer.append(len(myString1[i]))
    return answer