n,h=map(int,input().split())
res=0
ls=list(map(int,input().split()))
for n in ls:
    if n>h:
        res+=2
    else:
        res+=1 

print(res)