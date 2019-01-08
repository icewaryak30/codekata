n,m=map(int,input().split())
if n<=100000 and m<=100000:
	for i in range(n+1,m):
		if i%2==1:
			print(i,end=" ")
