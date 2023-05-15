n= int(input())
step=1
total=1
while n>total:
    step+=1
    total+=step
gap=total-n
if step%2==0:
    print(step-gap,end='')
    print('/',end='')
    print(gap+1)
else:
    print(gap+1,end='')
    print('/',end='')
    print(step-gap)
