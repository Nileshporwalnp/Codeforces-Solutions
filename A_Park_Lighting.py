for t in range(int(input())):
    n,m=map(int,input().split())
    res=m*n//2 if m*n%2==0 else m*n//2+1
    print(res)