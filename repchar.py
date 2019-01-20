#ice
s=input()
l=[]
c=0
for i in s:
    l.append(s.count(i))
x=max(l)
for i in range(0,len(s)):
    if s.count(s[i])==x:
        c=c+1
        if c==1:
            print(s[i])
    
