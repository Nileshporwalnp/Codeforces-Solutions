n=int(input())
ls=list(map(int,input().split()))
mn=101
mx=0
mnp=0
mxp=0
for i,val in enumerate(ls):
    if mn>=val:mn,mnp=val,i
    if mx<val:mx,mxp=val,i
if mnp>mxp:
    print(n-mnp-1+mxp)
else:
    print(n-1-mnp-1+mxp)