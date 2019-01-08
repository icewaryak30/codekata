n=int(input())
i=2
c=0
if n<=10000:
	while i<n-1:
		if n%i==0:
			c=c+1
		i=i+1
	if c!=0:
		print("no")
	else:
		print("yes")
