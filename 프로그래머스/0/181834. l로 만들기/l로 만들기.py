def solution(myString):
    # 전부 소문자
    # a,b,c,d,e,f,g,h,i,j,k -> l
    # 방법1. 해당 알파벳을 전부 replace를 사용해서 l로 변경하기
    myString = myString.replace('a','l')
    myString = myString.replace('b','l')
    myString = myString.replace('c','l')
    myString = myString.replace('d','l')
    myString = myString.replace('e','l')
    myString = myString.replace('f','l')
    myString = myString.replace('g','l')
    myString = myString.replace('h','l')
    myString = myString.replace('i','l')
    myString = myString.replace('j','l')
    myString = myString.replace('k','l')

    return myString