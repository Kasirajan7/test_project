n=int(input("Enter the array size"))
print("Enter the elements")
a=[int(input()) for i in range(n**2)]
b=[[0 for x in range(n)] for y in range(n)]
d=int(input("Enter number of rotations"))
k=0
f=d%4
if f==0:
        l1=0
        x1=0
        for i in range(n):
            y1=0
            for j in range(n):
                b[x1][y1]=a[l1]
                l1+=1
                y1+=1
            x1+=1
        print(b)
else:
    while (k<f):
        y=n-1
        l=0
        for i in range(n):
            x=0
            for j in range (n):
                b[x][y]=a[l]
                l+=1
                x+=1
            y-=1
        print(b)
        l1=0
        x1=0
        for i in range(n):
            y1=0
            for j in range(n):
                a[l1]=b[x1][y1]
                l1+=1
                y1+=1
            x1+=1
        k+=1
