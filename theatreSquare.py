n,m,k=map(int,input().split())
ln=n//k
if n%k!=0:ln+=1 
bre=m//k
if m%k!=0:bre+=1
print(ln*bre)
