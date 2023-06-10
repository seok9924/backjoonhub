a=input()
b=input()

if len(a)>=len(b):
    pass
else:
    a,b=b,a
count=0
s=''
for i in range(len(a)):
    if a[i] in b:
        s+=a[i]
        b=b.replace(a[i],'',1)

print(len(a)+len(b)-len(s))