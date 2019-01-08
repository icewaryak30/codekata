n=int(input())
j=list(map(int,input().split()))
g=sorted(j)
h=(len(g)+1)//2
print(g[h-1])
