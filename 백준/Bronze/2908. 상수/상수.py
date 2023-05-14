a,b=input().split()
a,b=int(''.join(list(reversed(a)))),int(''.join(list(reversed(b))))
print(a) if a>b else print(b)