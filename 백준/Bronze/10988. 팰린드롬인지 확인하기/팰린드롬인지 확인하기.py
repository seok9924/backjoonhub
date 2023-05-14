s=input()
flag=True
length=len(s)
for i in range(length):
    if s[i]!=s[length-1-i]:
        print(0)
        flag=False
        break

if flag:
    print(1)