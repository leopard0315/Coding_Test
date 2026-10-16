def solution(myStr):
    # 새로운 접근 : a,b,c 순서대로 문자열을 구분하는것이 아닌 구분자를 전부 한글자로 대체한다음에 해당 문자를 기준으로 쪼개면 된다.
    myStr = myStr.replace('a',' ').replace('b',' ').replace('c',' ')
    myStr_split = myStr.split() # split()으로 사용하게 되면 공백을 기준으로 자동으로 쪼개진다.
    
    if not myStr_split: # 만약 해당 리스트가 비어있다면 false 반환 -> not false == True(참)
       myStr_split.append('EMPTY')
    
    return myStr_split