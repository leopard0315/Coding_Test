# 백준 4949번
# 균형잡힌 세상

import sys
input = sys.stdin.readline

# 입력
while (1):
    N = input()
    answer = ""
    if N.rstrip() == ".":
        break
    else:
        a = [] # 소괄호 & 대괄호 순서 중요
        for i in range(len(N)):
            if N[i] == "(":
                a.append(N[i])

            elif N[i] == ")":
                if a and (a[-1] == "(") :
                    a.pop()
                else:
                    answer = "No"
                    break

            elif N[i] == "[":
                a.append(N[i])

            elif N[i] == "]":
                if a and (a[-1] == "["):
                    a.pop()
                else:
                    answer = "No"
                    break
            else:
                continue
        # 출력
        if len(a) == 0 and answer == "":
            print("yes")
        else :
            print("no")