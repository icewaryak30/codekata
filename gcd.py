#ice
n,k=map(int,input().split())
for i in range(1,(n*k)):
    if n%i==0 and k%i==0:
        j=i
print(j)
