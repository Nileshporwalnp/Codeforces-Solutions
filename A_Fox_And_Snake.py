r,c=map(int,input().split())
f='#'*c
l='.'*(c-1)+'#'
l2='#'+'.'*(c-1)
fl=True
for i in range(r//2):
    print(f)
    if fl:
        print(l)
        fl=False
    else:
        print(l2)
        fl=True

print(f)