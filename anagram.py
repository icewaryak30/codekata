#ice
n=int(input())
x="kabali"
s=[]
c,d=0,0
for i in range(n):
    s.append(input())
for i in s:
    if i==x:
        d=d+1
    elif len(i)==len(x):
        for j in i:
            if j in x:
                c+=1
        if c==len(i):
            d=d+1
print(d)
