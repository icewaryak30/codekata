n,k=map(int,input().split())
c=0
for b in range(n+1,k):
	for j in range(2,b):
		if b%j==0:
			c=c+1
			break
	else:
		print(b,end=" ")
