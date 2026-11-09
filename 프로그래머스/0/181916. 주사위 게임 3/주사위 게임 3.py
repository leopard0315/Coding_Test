def solution(a, b, c, d):
    score = 0
    A = [a,b,c,d]
    A.sort() # 오름차순 정렬
    
    # 모두 p로 같은 경우
    if A[0] == A[3]:
        return 1111 * A[0]
    # 세 주사위에서 나온 숫자가 p로 같은 경우
    if A[0] == A[2]:
        return (10 * A[0] + A[3]) ** 2
    elif A[1] == A[3]:
        return (10 * A[1] + A[0]) ** 2
    # 두 주사위가 2개씩 같은 값이 나오는 경우
    if A[0] == A[1] and A[2] == A[3]:
        return (A[0] + A[2]) * abs(A[2]-A[0])
    
    # 두 주사위에서 나온 숫자가 p로 같고 나머지가 q,r인 경우
    if A[0] == A[1]:
        return A[2] * A[3]
    elif A[1] == A[2]:
        return A[0] * A[3]
    elif A[2] == A[3]:
        return A[0] * A[1]
    else:
        return A[0]
    