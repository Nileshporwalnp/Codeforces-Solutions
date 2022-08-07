for _ in range(int(input())):
    n=int(input())
    if n%2==0:
        for i in range(n,0,-1):
            print(i,end=' ')
    else:
        print(n//2+1,end=' ')
        for i in range(n,0,-1):
            if i!=(n//2+1):
                print(i,end=' ')
    print()
    