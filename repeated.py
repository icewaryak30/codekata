#ice
n=int(input())
l=list(map(int,input().split()))
d={ }
k=[]
for i in l:
    s=l.count(i)
    d.update({i:s})
    k.append(s)
m=max(k)
if m==1:
    print("unique")
else:
    c=0
    for x,y in d.items():
        if y!=1:
            c+=1
            if c==1:
                print(x,end="")
            else:
                print("",x,end="")
