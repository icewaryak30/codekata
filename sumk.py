n,k=map(int,input().split())
x=[int(i) for i in input().split()]
if n>=k:
	s=[]
	for i in range(0,k):
		s.append(x[i])
	print(sum(s))
