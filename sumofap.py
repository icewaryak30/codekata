a,d,n=map(int,input().split())
l=a+(n-1)*d
s=str(((a+l)/2)*n)
for i in s:
    if s[-1]=="0":
        print(s[0:-2])
        break
    else:
        print(s)
        break
