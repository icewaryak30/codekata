x="kabali"
n=int(input())
s=[]
d=0
for i in range(n):
    s.append(input())
for i in s:
    if i==x:
        d=d+1
    elif len(i)==len(x):
        for j in i:
            c=0
            if j in x:
                if i.count(j) == x.count(j):
                    c+=1
        if c==len(i):
            d=d+1
print(d)
