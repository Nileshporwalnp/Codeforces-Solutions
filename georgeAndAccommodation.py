n=int(input())
res=0
for i in range(n):
    p,space=map(int,input().split())
    if space-p>=2:
        res+=1
print(res)