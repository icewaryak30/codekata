#ice
r,s=map(str,input().split())
k=int(s)
for i in range(0,k):
    if i==k-1:
        print(r[i])
    else:
        print(r[i],end="")
