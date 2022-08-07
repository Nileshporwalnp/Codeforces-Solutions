for t in range(int(input())):
    n=int(input())
    res=1
    if n==1 or n==2 or n==3:
        print(1)
    else:
        if n%2==0:
            print(n//2)
        else:
            print((n-1)//2)
    