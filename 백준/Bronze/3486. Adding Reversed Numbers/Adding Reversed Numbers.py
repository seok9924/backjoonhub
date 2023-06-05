n=int(input())

for i in range(n):
    a,b=input().split()
    a=a[::-1]
    b=b[::-1]
    while True:
        if a[0]!='0':
            break
        else:
            a.replace('0','',1)
    while True:
        if b[0] != '0':
            break
        else:
            a.replace('0', '', 1)

    answer=int(a)+int(b)
    answer=str(answer)[::-1]
    while True:
        if answer[0] != '0':
            break
        else:
            answer=answer.replace('0', '', 1)
    print(answer)