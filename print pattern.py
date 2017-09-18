b= [[None]*7]*7
k=0
n=7
#print(a)
for i in range(7):
    for j in range(7):        
        if i==k or j==k or i==n-1 or j==n-1:
            b[i][j]="4"
            #print("i=",i,"j=",j,a[i][j])
        elif i==k+1 or j==k+1 or i==n-2 or j==n-2:
            b[i][j]="3"
            #print("i=",i,"j=",j,a[i][j])
        elif i==k+2 or j==k+2 or i==n-3 or j==n-3:
            b[i][j]="2"
            #print("i=",i,"j=",j,a[i][j])
        else:
            b[i][j]="1"
            #print("i=",i,"j=",j,a[i][j])


for i in range(7):
    for j in range(7):
        print(b[i][j],end=" ")
    print(" ")

