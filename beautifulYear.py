from collections import Counter 
n=int(input())
def isBeautiful(k):
    d=Counter(k)
    if len(d)<4:
        return False
    return True
while True:
    n+=1
    if isBeautiful(str(n)):
        print(n)
        break
