ls=[0]*26
n=int(input())
s=input()
for i in s:
    ls[ord(i.lower())-97]=1
if sum(ls)==26:print("YES")
else:print("NO")


