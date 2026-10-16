def solution(myStr):
    # 새로운 접근 : a,b,c 순서대로 문자열을 구분하는것이 아닌 구분자를 전부 한글자로 대체한다음에 해당 문자를 기준으로 쪼개면 된다.
    
    # a,b,c구분자 전부 공백으로 대체
    myStr = myStr.replace('a',' ').replace('b',' ').replace('c',' ')
    # split()으로 사용하게 되면 공백을 기준으로 쪼개진다.
    myStr_split = myStr.split() 
    
    # 만약 해당 리스트가 비어있지않다면 myStr_split반환
    # 비어있다면 False 반환 -> 식을 만족하지않아서 else구문으로 가서 ['EMPTY'] 반환
    return myStr_split if myStr_split else ['EMPTY']