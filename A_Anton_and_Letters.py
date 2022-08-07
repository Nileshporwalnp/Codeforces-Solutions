s=input()
k=set()
for i in s:
    if i>='a' and i<='z':
        k.add(i)
print(len(k))