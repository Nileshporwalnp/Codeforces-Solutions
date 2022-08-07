c=1
ls=[]
for _ in range(int(input())):
    k=input()
    if len(ls)!=0 and ls[-1]!=k:
        c+=1
    ls.append(k)
print(c)

    