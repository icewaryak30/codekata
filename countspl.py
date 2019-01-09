s=input()
c=0
for i in s:
	if i.isalnum() or i==" ":
		pass
	else:
		c=c+1
print(c)
