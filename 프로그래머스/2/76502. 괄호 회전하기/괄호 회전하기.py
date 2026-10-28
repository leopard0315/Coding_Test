def solution(s):
    def valid(x):
        stack = []
        for ch in x:
            if ch in "([{":
                stack.append(ch)
            elif not stack or {')':'(',']':'[','}':'{'}[ch] != stack.pop():
                return False
        return not stack
    return sum(valid(s[i:]+s[:i]) for i in range(len(s)))