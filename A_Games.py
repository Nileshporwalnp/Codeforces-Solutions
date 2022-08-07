n=int(input())
res=0
h=[0]*n

for i in range(n):
    h,g=map(int,input().split())
    home[h]=1
    guest[g]=1
    ls.append((h,g))
print(res)