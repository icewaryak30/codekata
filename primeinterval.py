n,k=map(int,input().split())
c=0
l=[]
for b in range(n+1,k):
	for j in range(2,b):
		if b%j==0:
			c=c+1
			break
	else:
		l.append(b)
for x in range(0,len(l)):
	if x==0:
		print(l[x],end="")
	else:
		print(" ",l[x],end="")
