s1=input()
s2=input()
ls=list(s1)
for i in range(len(s1)):
    if s1[i]!=s2[i]:
        ls[i]='1'
    else:
        ls[i]='0'
print(''.join(ls))