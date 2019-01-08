n=int(input())
rev,rem=0,0
num=n
if n<=10000:
	while n!=0:
		rem=n%10
		rev=rev+pow(rem,3)
		n=n//10
	if rev==num:
		print("yes")
	else:
		print("no")
