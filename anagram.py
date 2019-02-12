#ice
n=int(input())
x="kabali"
s=[]
d=0
for i in range(n):
	s.append(input())
for i in s:
	c=0
	for j in i:
		if j in x:
			if i.count(j)==x.count(j):
				c=c+1
	if c==len(i):
		d=d+1
print(d)
