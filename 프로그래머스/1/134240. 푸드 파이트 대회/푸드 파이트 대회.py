## reverse() 함수
    # reverse() 함수는 문자열에서는 안된다.
    # 배열안에서 가능하다.
## 아이디어 접근
    # 0을 기준으로 앞이랑 뒤가 동일하니까 
    # 1) 앞을 구한다.
    # 2) 0을 넣는다.
    # 3) 앞의 문자열을 뒤집어서 더한다. - reverse()함수를 이용해서 뒤집는다.
    
# 방법1 - reverse()함수 사용해서 뒤집기
def solution(food):
    answer = ''
    # '0'전까지의 문자열을 구한다.
    for i in range(1,len(food)):
        answer += str(i) * (food[i]//2)
        
    # reverse()함수를 이용하기 위해서 리스트로 변환후에 뒤집고 다시 문자열로 변환
    l_ans = list(answer)
    l_ans.reverse()
    
    # 문자열 합치기
    return answer + '0' + ''.join(l_ans)

# 방법2 - 문자열 슬라이싱[::-1] 해주기
def solution(food):
    answer = ''
    # '0'전까지의 문자열을 구한다.
    for i in range(1,len(food)):
        answer += str(i) * (food[i]//2)
        
    # 문자열 슬라이싱이용해서 바로 뒤집기
    return answer + '0' + answer[::-1]