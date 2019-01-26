#ice
s=input()
c=0
for i in s:
    if i.isdigit():
        c=c+1
        if c==len(s):
            print("yes")
    else:
        print("no")
        break
