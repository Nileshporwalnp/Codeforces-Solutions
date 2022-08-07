n=int(input())
hate='I hate it'
love='I love it'
l='I love that'
h='I hate that'
ls=[]
for i in range(1,n+1):
    if i==n:
        if i%2==0:
            ls.append(love)
        else:
            ls.append(hate)
    elif i%2==1:
        ls.append(h)
    else:
        ls.append(l)
print(' '.join(ls))
