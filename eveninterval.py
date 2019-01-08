n,m=map(int,input().split())
l=[]
if n<=100000 and m<=100000:
	for i in range(n+1,m):
		if i%2==0:
			l.append(i)
	for k in range(0,len(l)):
		if k==0:
			print(l[k],end="")
		else:
			print(" ",l[k],end="")
