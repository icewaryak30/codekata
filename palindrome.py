n=int(input())
rev,rem=0,0
num=n
if n<=1000:
	while n!=0:
		rem=n%10
		rev=rem+rev*10
		n=n//10
	if rev==num:
		print("yes")
	else:
		print("no")
