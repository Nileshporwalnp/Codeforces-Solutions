for _ in range(int(input())):
    n=int(input())
    print(n)
    ls=[]
    k=[i for i in range(1,n+1)]
    ls.append(k)
    for i in range(1,len(k)):
        temp=k.copy()
        temp[i-1],temp[i]=temp[i],temp[i-1]
        ls.append(temp)
        k=temp.copy()
    for i in ls:
        for j in i:
            print(j,end=' ')
        print()