for _ in range(int(input())):
    n,m,k=map(int,input().split())
    if n==1 and m==1 and k==0:
        print("YES")
    elif ((n-1)+(m-1)*n)==k:print('YES')
    else:print('NO')