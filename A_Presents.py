n=int(input())
ls=list(map(int,input().split()))
res=[0]*len(ls)
for i,val in enumerate(ls):
    res[val-1]=i+1
for ans in res:
    print(ans,end=' ')