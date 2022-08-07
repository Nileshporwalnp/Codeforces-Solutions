indI=0
indJ=0
ls=[]
for i in range(5):
    k=list(map(int,input().split()))
    ls.append(k)
for i in range(5):
    for j in range(5):
        if ls[i][j]==1:
            indI=i
            indJ=j
            break
print(abs(2-indI)+abs(2-indJ))

