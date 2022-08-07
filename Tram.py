n=int(input())
sm=0 
bt=0
at=0
for i in range(n):
    a,b=map(int,input().split())
    bt+=(b-a)
    sm=max(bt,sm)
print(sm)