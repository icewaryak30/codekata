#ice
s,t,k=map(str,input().split())
c=0
for i in range(len(s)):
    if s[i]!=t[i]:
        c=c+1
if c==int(k):
    print("yes")
else:
    print("no")
