n=int(input())
t,c,o,d,i=4,6,8,12,20
res=0
for _ in range(n):
    s=input()
    if s=="Icosahedron":
        res+=i
    if s=='Cube':
        res+=c
    if s=="Octahedron":
        res+=o
    if s=='Tetrahedron':
        res+=t
    if s=='Dodecahedron':
        res+=d
print(res)


