def arms(n):
	r=0
	while n>0:
		rem=n%10
		r=r+pow(rem,3)
		n=n//10
	return r
n,k=map(int,input().split())
for i in range(n+1,k):
	num=i
	j=arms(i)
	if j==num:
		print(num)
