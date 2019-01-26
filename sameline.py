#ice
l=[]
c=0
for  i in range(3):
    l.append(input().split())
for i in range(3):
    if l[i][0]==l[0][0]:
        c=c+1
    elif l[i][1]==l[0][1]:
        c=c+1
if c==3:
    print("yes")
