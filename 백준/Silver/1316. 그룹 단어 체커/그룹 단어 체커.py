n=int(input())
ans=n
for i in range(n):
    s=input()
    for j in range(len(s)-1):
        if s[j]==s[j+1]:
            continue
        elif s[j] in s[j+1:]:
            ans-=1
            break
print(ans)