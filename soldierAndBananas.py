k,n,w=map(int,input().split())
total=w*(w+1)//2
dollar=total*k
if dollar<=n:
    print(0)
else:
    print(dollar-n)