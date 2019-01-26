#ice
n,k=map(int,input().split())
l=[]
l1=[i for i in input().split()]
l2=[i for i in input().split()]
for i in range(len(l2)):
    l1.append(l2[i])
    l.append(max(l1))
for i in range(len(l)):
    if i==0:
        print(l[i],end="")
    else:
        print("",l[i],end="")
