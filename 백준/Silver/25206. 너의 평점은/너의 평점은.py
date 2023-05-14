n=20
nsubject=20
d={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}


total=0
ns=0
for i in range(20):
    s,snumb,grade=input().split()
    if grade=="P":
        continue
    else:
       total+= d[grade]*float(snumb)
       ns+=float(snumb)
print(total/ns)