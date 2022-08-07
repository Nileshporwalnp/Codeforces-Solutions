s=input()
if len(s)==1:
    print(s)
else:
    ls=[]
    for i in range(0,len(s),2):
        ls.append(s[i])
    ls.sort()
    print('+'.join(ls))
