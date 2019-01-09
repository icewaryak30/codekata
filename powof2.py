#ice
n=int(input())
for i in range(1,1000):
    if 2**i==n:
        s="yes"
        break
    else:
        s="no"
print(s)
