for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(2)
    elif n%3==0:
        print(n//3)
    else:
        res=0
        while n>0 and n%3!=0:
            res+=1
            n-=2
        print(res+n//3)