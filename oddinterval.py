n,m=map(int,input().split())
if n<=100000 and m<=100000:
	for i in range(n,m+1):
		if i%2==1:
			print(i,end=" ")
