#ice
n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for i in range(len(l)):
    if i==0:
        print(l[i],end="")
    else:
        print("",l[i],end="")
