l=int(input("Enter the odd number of rows to print "))

n=1
count=1
a=int(l/2)
b=1
for i in range(l):
    k=0
    j=0
    if i<=l/2:
        while j<a :
            print(" ",end=" ")
            j=j+1
        a-=1
        while k<n:
            print("*",end=" ")
            count+=1
            k+=1
        n+=2
    else:
        if n==l+2:
            n=n-2
        while j<b:
            print(" ",end=" ")
            j=j+1
        b=b+1
        n-=2
        while k<n:
            print("*",end=" ")
            count+=1
            k+=1
    print("")
