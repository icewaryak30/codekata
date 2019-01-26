#ice
def squares(a, b):
    l=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 l.append(i)  
            j = j+1
        i = i+1
    return len(l)
x,y=map(int,input().split())
print(squares(x,y))
