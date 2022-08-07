from collections import Counter
s=input()
d=Counter(s)
if len(d)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
