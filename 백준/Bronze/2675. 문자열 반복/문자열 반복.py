t=int(input())

for i in range(t):
    multi,QR=input().split()
    s=''
    for qr in QR:
       s+=(int(multi)*qr)
    print(s)
