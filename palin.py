#ice
s=input()
s=s.casefold()
r=reversed(s)
if  list(s)==list(r):
    print("yes")
else:
    print("no")
