n=int(input())
c=0
x=[]
for i in range(n,1000000):
	if i%n==0:
		c=c+1
		x.append(i)
		if len(x)==5:
			break
for k in range(0,len(x)):
	if k==0:
		print(x[k],end="")
	else:
		print("",x[k],end="")
