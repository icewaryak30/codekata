n,k=map(int,input().split())
l=[int(i) for i in input().split()]
for i in range(0,len(l)+1):
    if i+1==k:
        print(l[i])
