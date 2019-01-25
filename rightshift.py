#ice
n,k=map(int,input().split())
x=[i for i in input().split()]
for _ in range(k):
    a=x[-1]
    x.remove(a)
    x.insert(0,a)
for i in range(len(x)):
    if i==0:
        print(x[i],end="")
    else:
        print("",x[i],end="")
