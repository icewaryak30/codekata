n=int(input())
x=[int(i) for i in input().split()]
c=sorted(x)
for i in range(0,len(c)):
	if i==0:
		print(c[i],end="")
	else:
		print("",c[i],end="")
	
