s=input()
x=[]
for i in s:
    if i.isupper():
        x.append(i.lower())
    else:
        x.append(i.upper())
for i in x:
    print(i,end="")
