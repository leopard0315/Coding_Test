A,B,V = input().split() # 공백 입력 받기
A = int(A) # 형변환
B = int(B)
V = int(V)
days = (V-A) // (A-B)
if (V-A) % (A-B) != 0 :
    days += 1
print(days+1)