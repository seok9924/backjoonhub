import math
a,b,v = map(int,input().split())

t= (v-b)/(a-b)

print(math.ceil(t))