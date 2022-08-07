s=int(input())
s=str(s)
c=0
for i in s: c=c+1 if i=='7' or i=='4' else c
if c==7 or c==4:
    print("YES")
else:
    print("NO")
