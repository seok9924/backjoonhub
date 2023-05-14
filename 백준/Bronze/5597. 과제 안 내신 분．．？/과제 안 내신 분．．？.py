a=[]
for i in range(28):
    a.append(int(input()))

b=[]
for i in range(1,31):
    if i not in a:
        b.append(i)
print(min(b))
print(max(b))