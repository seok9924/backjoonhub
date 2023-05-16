def solution(s):
    stack=[]
    for i in range(len(s)):
        if s[i]=="(":
            stack.append(")")
            continue
        if stack and stack[-1]==s[i] :
            stack.pop()
            continue
        else: 
            stack.append(s[i])
    if stack:
        return False
    else: 
        return True