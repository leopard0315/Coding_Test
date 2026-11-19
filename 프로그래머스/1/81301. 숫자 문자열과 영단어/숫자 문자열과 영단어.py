def solution(s):
    # # 방법1
    # s = s.replace('zero','0')
    # s = s.replace('one','1')
    # s = s.replace('two','2')
    # s = s.replace('three','3')
    # s = s.replace('four','4')
    # s = s.replace('five','5')
    # s = s.replace('six','6')
    # s = s.replace('seven','7')
    # s = s.replace('eight','8')
    # s = s.replace('nine','9')
    # return int(s)

    # 방법2
    dict = {'zero':'0', 'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    
    for key, value in dict.items():
        s = s.replace(key,value)
    return int(s)

# dictionary - items()
# items()를 사용하게 되면 key와 value를 한꺼번에 뽑을 수 있다.