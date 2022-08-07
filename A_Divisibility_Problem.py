for _ in range(int(input())):
    a,b=map(int,input().split())
    res=0
    if a%b==0:
        print(res)
    else:
        d=a//b
        print(b*(d+1)-a)