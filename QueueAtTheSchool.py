n,t=map(int,input().split())
s1=input()
s=list(s1)
i=0
if n==1:
    print(s1)
else:
    while t>0:
        i=0
        while i+1<n:
            if s[i]=='B':
                k=s[i+1]
                s[i],s[i+1]=s[i+1],s[i]
                if k!='B':
                    i+=1
            i+=1 
        t-=1
    print(''.join(s))

