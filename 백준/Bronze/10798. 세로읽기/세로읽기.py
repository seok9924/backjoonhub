n=5
s=''
all=[]
for i in range(n):
    all.append(list(map(str,input())))

for i in range(15):
    for j in range(n):
        try:
          s+=all[j][i]
        except:
            continue
print(s)
