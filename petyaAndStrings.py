
s1=input()
s2=input()
flag=True
for i in range(len(s1)):
    if s1[i].lower() < s2[i].lower():
        print(-1)
        flag=False
        break
        
    if s1[i].lower() > s2[i].lower():
        print(1)
        flag=False
        break 
if flag:
    print(0)