#ice
s=input()
c=[]
for i in s:
    if i=="(":
        c.append(1)
    elif i==")":
        c.append(-1)
if sum(c)==0:
    print("yes")
else:
    print("no")
